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
        "Apple",
        "Banana",
        "Orange",
        "Apple",
        "Grape",
        "Banana",
        "Mango",
        "Apple",
        "Orange"
    ]
    fruit_groups = group_fruits(sample_fruits)
    for fruit_type, fruits in fruit_groups.items():
        print(f"{fruit_type}: {sorted(list(set(fruits)))}")