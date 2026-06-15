def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        if fruit in grouped:
            grouped[fruit].append(fruit)
        else:
            grouped[fruit] = [fruit]
    return grouped
if __name__ == '__main__':
    fruits = [
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
    fruit_groups = group_fruits(fruits)
    for fruit_type, fruit_list in fruit_groups.items():
        print(f"{fruit_type}: {', '.join(sorted(list(set(fruit_list))))}")