def count_fruits(fruit_list):
    counts = {}
    for fruit in fruit_list:
        if isinstance(fruit, str) and len(fruit.strip()) > 0:
            type_name = "fresh" if "-" not in fruit else "processed"
            counts[type_name] = counts.get(type_name, 0) + 1
    return counts
if __name__ == '__main__':
    sample_fruits = ["apple", "-banana", "orange", "grape"]
    result = count_fruits(sample_fruits)
    print(result)