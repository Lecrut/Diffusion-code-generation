def count_fruits(fruit_list):
    counts = {}
    for fruit in fruit_list:
        if isinstance(fruit, str) and len(fruit.strip()) > 0:
            counts[fruit] = counts.get(fruit, 0) + 1
    return counts
if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "orange", "apple", "grape"]
    result = count_fruits(sample_fruits)
    print(result)