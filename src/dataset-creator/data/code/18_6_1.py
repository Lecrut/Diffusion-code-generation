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
        "Banana",
        "Apricot",
        "Berry",
        "Carrot",
        "Coconut",
        "Avocado",
        "Grape"
    ]
    result = group_fruits(sample_fruits)
    print(result)
    empty_test = []
    empty_result = group_fruits(empty_test)
    print(f"Empty test result: {empty_result}")