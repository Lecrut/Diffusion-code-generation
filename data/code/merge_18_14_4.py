import collections
def group_fruits(fruit_list):
    grouped = collections.defaultdict(list)
    for fruit in fruit_list:
        fruit_type = fruit.lower().split()[0]
        if fruit_type:
            grouped[fruit_type].append(fruit)
        else:
            print(f"Error: Invalid fruit entry encountered: {fruit}")
    return dict(grouped)
if __name__ == '__main__':
    sample_fruits = [
        "apple",
        "banana",
        "orange",
        "grape",
        "mango",
        "apricot",
        "kiwi",
        "watermelon",
        "peach",
        "melon",
        "strawberry",
        "invalid fruit entry"
    ]
    grouped_results = group_fruits(sample_fruits)
    print("--- Grouped Fruits ---")
    for fruit_type, fruits in grouped_results.items():
        print(f"\n{fruit_type}:")
        for fruit in fruits:
            print(f"- {fruit}")