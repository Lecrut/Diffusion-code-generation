def categorize_animals(animal_list):
    animal_categories = {'mammal': ['dog', 'cat', 'lion', 'elephant'], 'bird': ['bird'], 'reptile': ['snake', 'turtle']}
    category_map = {animal: category for category, animals in animal_categories.items() for animal in animals}
    result = {}
    for animal in animal_list:
        if animal not in category_map:
            category_map[animal] = 'other'
        result[animal] = category_map[animal]
    return result
if __name__ == '__main__':
    sample_animals = ['dog', 'cat', 'bird', 'snake', 'fish', 'lion']
    organized_data = categorize_animals(sample_animals)
    print(organized_data)