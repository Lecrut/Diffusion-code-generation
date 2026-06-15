import random
def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        if fruit in grouped:
            grouped[fruit].append(fruit)
        else:
            grouped[fruit] = [fruit]
    return grouped
if __name__ == '__main__':
    sample_fruits = [
        "apple",
        "banana",
        "orange",
        "apple",
        "grape",
        "banana",
        "mango",
        "kiwi",
        "watermelon",
        "apple",
        "lemon",
        "invalid_fruit"
    ]
    valid_fruits = []
    invalid_fruits = []
    for fruit in sample_fruits:
        if fruit in ["apple", "banana", "orange", "grape", "mango", "kiwi", "watermelon", "lemon"]:
            valid_fruits.append(fruit)
        else:
            invalid_fruits.append(fruit)
    grouped_result = group_fruits(valid_fruits)
    print("--- Grouped Fruits ---")
    if grouped_result:
        for fruit_type, fruits in grouped_result.items():
            print(f"{fruit_type}: {', '.join(sorted(list(set(fruits))))}")
    else:
        print("No valid fruits found to group.")
    print("\n--- Invalid Entries ---")
    if invalid_fruits:
        for fruit in invalid_fruits:
            print(f"Error processing: {fruit}")
    else:
        print("No invalid entries found.")