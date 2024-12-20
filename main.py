class student:
    grade = 10
    print("hi i am a student of grade", grade)
ob = student
class vehicle:
    def ___init___(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = vehicle(240, 18)
print("model max speed:", modelX.max_speed)
print("model mileage:", modelX.mileage)
class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = parrot("blu", 10)
woo = parrot("woo", 15)
print("blu is a {}".format(blu.species))
print("woo is also a {}".format(woo.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))
