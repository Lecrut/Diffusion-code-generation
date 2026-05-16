class AnimalList:
    def __init__(self, animals):
        self.animals = animals
    def insert_animal(self, new_animal):
        n = len(self.animals)
        self.animals.insert(n, new_animal)
if __name__ == '__main__':
    initial_animals = ["Dog", "Cat", "Bird"]
    animal_list = AnimalList(initial_animals)
    print(f"Initial list: {animal_list.animals}")
    new_animal = "Fish"
    animal_list.insert_animal(new_animal)
    print(f"After inserting {new_animal}: {animal_list.animals}")
    new_animal_2 = "Snake"
    animal_list.insert_animal(new_animal_2)
    print(f"After inserting {new_animal_2}: {animal_list.animals}")