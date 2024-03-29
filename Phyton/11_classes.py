# -*- coding: utf-8 -*-
"""11_Classes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IczXwe4hD_SUCQBjOl4z7GS8BDBGUNTy
"""

### Classes ###

# Definicion

class MyEmptyPerson:
  pass #Para poder dejar la clave vacia

print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con contructor, funciones y propiedades privadas y publicas


class Person:
  def _init_(self, name, surname, alias="Sin alias"):
    self.full_name = f"{name} {surname} ({alias})" # Propiedad publica
    self._name = name # Propiedad privada
  def get_name (self):
    return self._name

  def walk(self):
    print(f"{self.full_name}esta caminando")

my_person = Person("Fermin","García")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Fermin", "Garcia", "GarciDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de leon"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)