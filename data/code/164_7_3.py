class AnimalList:
    def __init__(self, animals=None):
        self.animals = animals if animals is not None else []
    def insert_animal(self, animal_type):
        self.animals.append(animal_type)
if __name__ == '__main__':
    initial_animals = ["Dog", "Cat", "Bird"]
    animal_list = AnimalList(initial_animals)
    print(f"Initial list: {animal_list.animals}")
    new_animal = "Fish"
    animal_list.insert_animal(new_animal)
    print(f"After inserting {new_animal}: {animal_list.animals}")
    another_animal = "Snake"
    animal_list.insert_animal(another_animal)
    print(f"After inserting {another_animal}: {animal_list.animals}")