picker= 1
class CitaMedica:
    def __init__(self,fecha,motivo,diagnostico="Pendiente"):
        self.fecha=fecha
        self.motivo=motivo
        self.diagnostico=diagnostico
class pet:
    def __init__(self,namePet,Species,Raze,Age,Owner=0,citas=[]):
        self.namePet=namePet
        self.Species=Species
        self.Raze=Raze
        self.Age=Age
        self.Owner=Owner
        self.citas=[]
class owner:
    def __init__(self,name,phone,mail,pets=[]):
        self.name=name
        self.phone=phone
        self.mail=mail
        self.pets=[]


petlist=[]

ownlist= []
def PetInfo(pet=pet(0,0,0,0)):
        print("Nombre:",pet.namePet)
        print("Species:",pet.Species)
        print("Raze:",pet.Raze)
        print("Age:",pet.Age)
        if owner!=0:
            print("Dueño",pet.Owner)
def OwnerInfo(owner=owner(0,0,0,petlist)):
    print("Nombre:",owner.name)
    print("Telefono:",owner.phone)
    print("Email:",owner.mail)
def ViewPetsReg (owner=owner(0,0,0,petlist)):
    cont=0
    for pet in owner.pets:
        cont=cont+1
        print(pet.namePet)
while picker !=4:
    print("-----Menu Veterinario-----")
    print("1)Gestion clientes")
    print("2)Gestion mascotas")
    print("3)Citas medicas")
    print("4)Salir")
    picker= int(input("Seleccione una opcion:"))
    match picker:
        case 1:
            while picker != 4:
                print("-----Gestion de Clientes-----")
                print("1)Registrar nuevo Cliente")
                print("2)Ver Clientes registrados")
                print("3)Relacionar un Clientes con varias mascotas")
                print("4)Salir")
                picker = int(input("Seleccione una opcion:"))
                match picker:
                    case 1:
                        name = input("Ingrese el nombre de la persona:")
                        phone = int(input("Ingrese el numero de telefono"))
                        if (phone==int):

                            email = int(input("Ingrese el correo electronico:"))

                            Owner = owner(name, phone, email)
                            ownlist.append(Owner)
                        elif (phone!=int):
                            print("Numero Invalido")
                        picker=1
                    case 2:
                        ContentList=ownlist.count()
                        if ContentList!=0:
                            cont=0
                            for owner in ownlist:
                                cont=cont+1
                                print(cont,")")
                                OwnerInfo(owner)
                        elif ContentList==0:
                            print("No existen Clientes registrados")
                    case 3:
                        ContentListOwn = ownlist.count()
                        ContentListPet = petlist.count()
                        if ContentListPet != 0&ContentListOwn != 0:
                            cont = 0
                            for owner in ownlist:
                                cont = cont + 1
                                print(cont, ")",owner.name)
                            print("Ingrese el numero del Clientes al que desea asociar las mascotas:")
                            ownimput= int(input())
                            if ownimput>0:
                                petimuput=1
                                while(petimuput!=0):
                                    for pet in petlist:
                                        cont = cont + 1
                                        print(cont, ")", owner.name)
                                    print("Ingrese el numero de la mascota a la que desea asociar (escriba 0 para terminar):")
                                    petimput = int(input())
                                    if petimput>0:
                                        ownlist[ownimput+1].pets.append(petlist.pop(petimput-1))
                                    elif petimput<1:
                                        print("Opcion no valida")
                            elif ownimput<1:
                                print("Opcion no valida")
                        else:
                            if ContentListOwn==0:
                                print("No existen Clientes registrados")
                            if ContentListPet == 0:
                                print("No existen mascotas registradas")
            picker=0

        case 2:
            while picker != 4:
                print("-----Gestion de Mascotas-----")
                print("1)Registrar nueva mascota")
                print("2)Relacionar mascota con un Clientes")
                print("3)Ver Mascotas registrados por Cliente")
                print("4)Salir")
                picker = int(input("Seleccione una opcion:"))
                match picker:
                    case 1:
                        name = input("Ingrese el nombre de la mascota:")
                        Species = int(input("Ingrese la especie:"))
                        Raze = int(input("Ingrese la raza:"))
                        Age = int(input("Ingrese la edad:"))
                        if Age>0 or Age<60:
                            Pet= pet(name,Species,Raze,Age)

                        elif Age<0 and Age>60:
                            print("Edad invalida")

                        picker=1
                    case 2:
                        ContentListOwn = ownlist.count()
                        ContentListPet = petlist.count()
                        if ContentListPet != 0&ContentListOwn != 0:
                            cont = 0
                            for owner in ownlist:
                                cont = cont + 1
                                print(cont, ")",owner.name)
                            print("Ingrese el numero del Cliente al que desea asociar las mascotas:")
                            ownimput = int(input())
                            if ownimput > 0:
                                ownimput= int(input())
                            if ownimput>0:
                                petimuput=1
                                for pet in petlist:
                                    cont = cont + 1
                                    print(cont, ")", owner.name)
                                print("Ingrese el numero de la mascota a la que desea asociar:")
                                petimput = int(input())
                                if petimput>0:
                                    ownlist[ownimput+1].pets.append(petlist.pop(petimput-1))
                    case 3:
                        ContentListOwn = ownlist.count()
                        ContentListPet = petlist.count()
                        if ContentListPet != 0&ContentListOwn != 0:
                            cont = 0
                            for owner in ownlist:
                                cont = cont + 1
                                print(cont, ")",owner.name)
                            print("Ingrese el numero del Cliente al que desea asociar las mascotas:")
                            ownimput = int(input())

                            if ownimput>0:
                                petimuput=1
                                while(petimuput!=0):
                                    for pet in petlist:
                                        cont = cont + 1
                                        print(cont, ")", owner.name)
                                    print("Ingrese el numero de la mascota a la que desea asociar (escriba 0 para terminar):")
                                    petimput = int(input())
                                    if petimput>0:
                                        ownlist[ownimput+1].pets.append(petlist.pop(petimput-1))
                            elif petimput<1:
                                print("Opcion no valida")
                        else:
                            if ContentListOwn==0:
                                print("No existen Clientes registrados")
                            if ContentListPet == 0:
                                print("No existen mascotas registradas")
            picker=0
        case 3:
            print("-----Gestion de Mascotas-----")
            print("1)Registrar nueva mascota")
            print("2)Relacionar mascota con un Clientes")
            print("3)Ver Mascotas registrados por Cliente")
            print("4)Salir")
            picker = int(input("Seleccione una opcion:"))
            match picker:
                case 1:
                    ContentListPet = petlist.count()
                    if ContentListPet != 0:
                        cont = 0
                        for owner in ownlist:
                            cont = cont + 1
                            print(cont, ")", owner.name)
                        print("Ingrese el numero del Cliente al que desea ver las mascotas:")
                        ownimput = int(input())
                        if ownimput > 0:
                            petimuput = 1
                            for pet in petlist:
                                cont = cont + 1
                                print(cont, ")", owner.name)
                            print("Ingrese el numero de la mascota a la que agendar una consulta")
                            petimput = int(input())
                            if petimput > 0&petimput <= ContentListPet :
                                Date = int(input("Ingrese la fecha que estaria agendando la cita:"))
                                Reason = int(input("Ingrese el motivo por el que se realizara la cita:"))
                                ownlist[ownimput + 1].pets[petimput + 1].date = Date
                                ownlist[ownimput + 1].pets[petimput + 1].reason = Date
                        elif ownimput<1:
                            print("Opcion no valida")
                case 2:
                    ContentListPet = petlist.count()
                    if ContentListPet != 0:
                        cont = 0
                        for owner in ownlist:
                            cont = cont + 1
                            print(cont, ")", owner.name)
                        print("Ingrese el numero del Cliente al que desea asociar las mascotas:")
                        ownimput = int(input())

                        if ownimput > 0:
                            petimuput = 1
                            for pet in petlist:
                                cont = cont + 1
                                print(cont, ")", owner.name)
                            print("Ingrese el numero de la mascota a la que desea agendarle una cita:")
                            petimput = int(input())
                            if petimput > 0:
                                ownlist[ownimput + 1].pets.append(petlist.pop(petimput - 1))
                        elif ownimput<1:
                            print("Opcion no valida")
                case 3:
                    ContentListOwn = ownlist.count()
                    ContentListPet = petlist.count()
                    if ContentListPet != 0 & ContentListOwn != 0:
                        cont = 0
                        for owner in ownlist:
                            cont = cont + 1
                            print(cont, ")", owner.name)
                        print("Ingrese el numero del Cliente al que desea asociar las mascotas:")
                        ownimput = int(input())
                        if ownimput > 0:
                            ownimput = int(input())
                        if ownimput > 0:
                            petimuput = 1
                            while (petimuput != 0):
                                for pet in petlist:
                                    cont = cont + 1
                                    print(cont, ")", owner.name)
                                print(
                                    "Ingrese el numero de la mascota a la que desea asociar (escriba 0 para terminar):")
                                petimput = int(input())
                                if petimput > 0:
                                    ownlist[ownimput + 1].pets.append(petlist.pop(petimput - 1))
                    else:
                        if ContentListOwn == 0:
                            print("No existen Clientes registrados")
                        if ContentListPet == 0:
                            print("No existen mascotas registradas")
    picker = 0
