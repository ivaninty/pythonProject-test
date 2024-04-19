class boy:
    def __init__(self, name="Matviy",monay=1000,age = 19 ):
        self.name = name
        self.money = monay
        self.age = age



    def dowork(self):
        self.money += 1000


    def buycar(self):
        self.money -= 1500

    def walk_with_girl(self):
        self.money -= 300

    def present(self):
        self.money -= 200
stud = boy()

print("Гроші",stud.money)
print("Імя",stud.name)
print("Вік",stud.age)


stud.walk_with_girl()
print("Матвій погуляв з дівчиною, гроші =",stud.money)


stud.dowork()
print("Матвій пішов на роботу, гроші = ", stud.money)

stud.buycar()
print("Матвій купив машину, гроші = ", stud.money)

stud.dowork()
print("Матвій пішов на роботу, гроші = ", stud.money)

stud.present()
print("Матвій зробив подарунок мамі, гроші = ", stud.money)







