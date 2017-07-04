import random


class itPersonel:
    def __init__(self, name, salary, positon):
        self.name = name
        self.salary = salary
        self.position = positon

    def __str__(self):
        return self.name + " " + self.position + " " + str(self.salary)


def increaseForAll(x):
    x.salary *= 1.15
    x.salary = int(x.salary)
    return x


def increaseForSome(x):
    x.salary *= 1.02
    x.salary = int(x.salary)
    return x

#
positions = ["Application Developer", "Customer Support Administrator", "Data Quality Manager",
             "Database Administrator",
             "IT Support Manager", "IT Systems Administrator", "Network Systems Administrator", "Security Specialist",
             "Software Engineer", "Technical Operations Officer"]

firstNames = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Charles"]
lastNames = ["Smith", "Johnson", "William", "Brown", "Jones", "Miller", "Davis"]

employees = []
name = ""

for i in range(0, 50, 1):
    name = firstNames[random.randrange(0, 8, 1)] + " " + lastNames[random.randrange(0, 7, 1)]
    salary = random.randrange(40000, 180000, 10000)
    employees.append(itPersonel(name, salary, positions[random.randrange(0, 10, 1)]))

#################Prvi zadatak#########################
print(employees[5])

employees = list(map(lambda x: increaseForAll(x), employees))

print(employees[5])
print("\n")
######################################################

#################Drugi zadatak########################
new_employes = list(filter(lambda x: x.salary < 60000, employees))
print(new_employes[5])

new_employes = list(map(lambda x: increaseForSome(x), list(filter(lambda x: x.salary < 60000, employees))))

print(new_employes[5])
print("\n")
######################################################

#################Treci zadatak########################
networkAndSystem = list(filter(lambda x:
                               x.position == "Network Systems Administrator" or
                               x.position == "IT Systems Administrator",
                               employees))

for item in networkAndSystem:
    print(item)
print("\n")
######################################################

#################Cetvrti zadatak######################

noTech = list(filter(lambda x: x.position != "Technical Operations Officer", employees))
for item in noTech:
    print(item)
print("\n")
