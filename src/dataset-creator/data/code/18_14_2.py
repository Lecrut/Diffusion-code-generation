import random
def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        fruit_lower = fruit.lower()
        if fruit_lower in grouped:
            grouped[fruit_lower].append(fruit)
        else:
            grouped[fruit_lower] = [fruit]
    return grouped
if __name__ == '__main__':
    sample_fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "apple",
        "mango",
        "banana",
        "kiwi",
        "strawberry",
        "apple",
        "watermelon",
        "pear",
        "invalid_fruit"
    ]
    valid_fruits = []
    for fruit in sample_fruits:
        if fruit.isalpha():
            valid_fruits.append(fruit)
    grouped_results = group_fruits(valid_fruits)
    print("Grouped Fruits:")
    for fruit_type, fruits in grouped_results.items():
        print(f"--- {fruit_type.capitalize()}:")
        for fruit in fruits:
            print(f"- {fruit}")
        print("")