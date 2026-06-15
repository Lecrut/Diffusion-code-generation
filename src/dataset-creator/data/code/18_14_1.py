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
        "strawberry",
        "kiwi",
        "watermelon",
        "apple"
    ]
    invalid_fruits = [
        "melon",
        "pear",
        "zucchini"
    ]
    all_fruits = sample_fruits + invalid_fruits
    processed_fruits = []
    for fruit in all_fruits:
        if fruit and fruit.isalpha():
            processed_fruits.append(fruit)
        else:
            print(f"Error: Invalid fruit entry ignored: {fruit}")
    grouped_result = group_fruits(processed_fruits)
    print("--- Grouped Fruits ---")
    if grouped_result:
        for fruit_type, fruits in grouped_result.items():
            print(f"\n{fruit_type.capitalize()}:")
            for fruit in sorted(fruits):
                print(f"- {fruit}")
    else:
        print("No valid fruits were processed.")