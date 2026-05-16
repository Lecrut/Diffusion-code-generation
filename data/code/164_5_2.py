import collections
def custom_sort_and_group(animal_list):
    sorted_list = sorted(animal_list)
    grouped_list = collections.defaultdict(list)
    for animal in sorted_list:
        first_letter = animal[0].upper()
        grouped_list[first_letter].append(animal)
    result = []
    for letter in sorted(grouped_list.keys()):
        result.extend(grouped_list[letter])
    return result
if __name__ == '__main__':
    animals = ["lion", "tiger", "elephant", "zebra", "monkey", "bear"]
    sorted_and_grouped = custom_sort_and_group(animals)
    print(sorted_and_grouped)