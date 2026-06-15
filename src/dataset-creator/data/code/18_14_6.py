import collections
def group_fruits(fruit_list):
    grouped = collections.defaultdict(list)
    for fruit in fruit_list:
        if fruit in grouped:
            grouped[fruit].append(fruit)
        else:
            grouped[fruit] = [fruit]
    return dict(grouped)
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
        "apple",
        "watermelon",
        "invalid_fruit"
    ]
    valid_fruits = []
    for fruit in sample_fruits:
        if fruit in ["apple", "banana", "orange", "grape", "mango", "kiwi", "watermelon"]:
            valid_fruits.append(fruit)
        else:
            print(f"Warning: Invalid fruit entry ignored: {fruit}")
    grouped_result = group_fruits(valid_fruits)
    print("--- Grouped Fruits ---")
    if grouped_result:
        for fruit_type, fruits in grouped_result.items():
            print(f"{fruit_type}: {', '.join(sorted(list(set(fruits))))}")
    else:
        print("No valid fruits were processed.")