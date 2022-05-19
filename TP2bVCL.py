import libvirt
import os
import sys


def hyper_name():
    print("Le nom de l'hyperviseur: " + conn.getHostname())


def vm_list():
    vm = conn.listAllDomains()
	print("Les machines virtuelles disponible: ")
    	for i in range(len(vm)):
        	print(vm[i].name())

def vm_start():
    vm_list()
    name = raw_input("entrer le nom de la machine que vous voulez demarrer : ")
    rhel = conn.lookupByName(name)
    rhel.create()
    os.system("virt-viewer " + rhel.name() + " &")


def vm_stop():
    vm_list
    name = raw_input("entrer le nom de la machine que vous voulez Arreter: ")
    rhel = conn.lookupByName(name)
    rhel.destroy()


def vm_ip():
    vm = conn.listDomainsID()
	if vm == None:
		print("Echec de l'obtention de la liste des ID de domaine")
		return 1
	for i in range(len(vm)):
		print("la machine virtuelle "+conn.lookupByID(vm[i]).name()+" de l'ID: "+str(i))
	choix = int(input("Entrer l'id de Votre choix : "))
	
	target = conn.lookupByID(vm[choix])
	print("L'adress IP de la machine virtuelle " + target.name() + " est : " +
		  target.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)['ens3']['addrs'][0]['addr'])

def quitter(conn):
    exit()

while True:
    conn = libvirt.open("qemu:///system")
    l = raw_input("\n \n")
    l =""
    Text = '''0) Nom de la machine hyperviseur\n
1) Lister les machines virtuelles\n
2) demarrer une machine \n
3) Arreter une machine \n
4) L adresse IP d une machine virtuelle donnee \n
5) Quitter\n'''
    print(Text)
    n = input("entrer le numero correspondant : ")
    if (n == 0):
        hyper_name()
    elif (n == 1):
        vm_list()
    elif (n == 2):
        vm_start()
    elif (n == 3):
        vm_stop()
    elif (n == 4):
        vm_ip()
    elif (n == 5):
        break
    else:
        print("entrer un nombre entre 0 et 5 ")


