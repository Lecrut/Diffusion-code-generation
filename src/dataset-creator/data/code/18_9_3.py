import collections
def group_fruits(fruit_list):
    grouped = collections.defaultdict(list)
    for fruit in fruit_list:
        grouped[fruit].append(fruit)
    return dict(grouped)
if __name__ == '__main__':
    sample_fruits = [
        "apple",
        "banana",
        "orange",
        "apple",
        "grape",
        "banana",
        "apple",
        "mango"
    ]
    result = group_fruits(sample_fruits)
    print("--- Fruit Grouping Result ---")
    for fruit, fruits in result.items():
        print(f"{fruit}: {', '.join(sorted(list(set(fruits))))}")