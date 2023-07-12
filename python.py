# multilevel inheritance.py
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Mammal(Animal):
    def give_birth(self):
        print(f"{self.name} is giving birth to live young.")


class NonMammal(Animal):
    def lay_eggs(self):
        print(f"{self.name} is laying eggs.")


class Cow(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def moo(self):
        print(f"{self.name} says 'Moo!'")


class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(f"{self.name} says 'Woof!'")


class Insect(NonMammal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} is flying.")


# Create instances and test the functionality

cow = Cow("Bessie")
cow.eat()  # Output: "Bessie is eating."
cow.sleep()  # Output: "Bessie is sleeping."
cow.give_birth()  # Output: "Bessie is giving birth to live young."
cow.moo()  # Output: "Bessie says 'Moo!'"

dog = Dog("Buddy")
dog.eat()  # Output: "Buddy is eating."
dog.sleep()  # Output: "Buddy is sleeping."
dog.give_birth()  # Output: "Buddy is giving birth to live young."
dog.bark()  # Output: "Buddy says 'Woof!'"

insect = Insect("Butterfly")
insect.eat()  # Output: "Butterfly is eating."
insect.sleep()  # Output: "Butterfly is sleeping."
insect.lay_eggs()  # Output: "Butterfly is laying eggs."
insect.fly()  # Output: "Butterfly is flying."
