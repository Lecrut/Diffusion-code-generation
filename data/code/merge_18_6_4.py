def group_fruits(fruit_list):
    if not fruit_list:
        return {}
    categories = {}
    for fruit in fruit_list:
        category = None
        if fruit.startswith('A'):
            category = 'Apple'
        elif fruit.startswith('B'):
            category = 'Banana'
        elif fruit.startswith('C'):
            category = 'Cherry'
        else:
            category = 'Other'
        if category not in categories:
            categories[category] = []
        categories[category].append(fruit)
    return categories
if __name__ == '__main__':
    sample_fruits = [
        "Apple",
        "Apricot",
        "Banana",
        "Blueberry",
        "Carrot",
        "Coconut",
        "Avocado",
        "Grape"
    ]
    grouped_result = group_fruits(sample_fruits)
    print(grouped_result)