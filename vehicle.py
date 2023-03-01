class Vehicle:
    def __init__(self,name,maxspeed,milage,color="white"):
        self.name = name
        self.maxspeed = maxspeed
        self.milage = milage
        self.color = color
        
    def seatingcapacity(self, capacity):
        print('seating capacity is {}'.format(capacity))
        
class Car(Vehicle):
     def seatingcapacity(self, capacity=4):
        super().seatingcapacity(capacity)
    
class Truck(Vehicle):
    def seatingcapacity(self, capacity=2):
        super().seatingcapacity(self.capacity)
    
class Bus(Vehicle):
     def seatingcapacity(self, capacity=5):
        super().seatingcapacity(self.capacity)


c = Car("audi",100,50)
print(c.seatingcapacity(10))
classes = c.__class__
print("the name of the class is {} the car name {} max speed {} milage {}the color is {}".format(classes.__name__ ,c.name,c.maxspeed,c.milage,c.color))

t = Truck("container",50,30)
classes = t.__class__
print("the name of the class is {} the truck name {} max speed {} milage {}the color is {}".format(classes.__name__ ,t.name,t.maxspeed,t.milage,t.color))

b = Bus("Schoolbus",40,60)
classes = b.__class__
print("the name of the class is {} the bus name {} max speed {} milage {}the color is {}".format(classes.__name__ ,b.name,b.maxspeed,b.milage,b.color))
