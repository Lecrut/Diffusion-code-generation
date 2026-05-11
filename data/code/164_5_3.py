import operator
def custom_sort_and_group(animal_list):
    sorted_list = sorted(animal_list)
    grouped_list = {}
    for animal in sorted_list:
        first_letter = animal[0]
        if first_letter not in grouped_list:
            grouped_list[first_letter] = []
        grouped_list[first_letter].append(animal)
    return sorted_list, grouped_list
if __name__ == '__main__':
    animals = ["lion", "tiger", "elephant", "zebra", "monkey", "giraffe", "bear"]
    sorted_animals, grouped_animals = custom_sort_and_group(animals)
    print(sorted_animals)
    print(grouped_animals)