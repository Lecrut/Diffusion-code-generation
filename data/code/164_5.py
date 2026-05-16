import operator
def custom_sort_and_group(animals):
    sorted_animals = sorted(animals)
    grouped_animals = {}
    for animal in sorted_animals:
        first_letter = animal[0]
        if first_letter not in grouped_animals:
            grouped_animals[first_letter] = []
        grouped_animals[first_letter].append(animal)
    return sorted_animals, grouped_animals
if __name__ == '__main__':
    animal_list = ["Lion", "Tiger", "Elephant", "Bear", "Zebra", "Giraffe", "Monkey"]
    sorted_list, grouped_data = custom_sort_and_group(animal_list)
    print(sorted_list)
    print(grouped_data)