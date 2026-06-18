def group_fruits(fruit_list):
    grouped = {}
    for fruit in fruit_list:
        if fruit in grouped:
            grouped[fruit].append(1)
        else:
            grouped[fruit] = [1]
    return grouped
if __name__ == '__main__':
    fruits = ["Apple", "Banana", "Orange", "Apple", "Grape", "Banana", "Mango"]
    result = group_fruits(fruits)
    for fruit, items in result.items():
        print(f"{fruit}: {len(items)} occurrences")