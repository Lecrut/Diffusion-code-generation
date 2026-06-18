def count_fruits(fruit_list):
    counts = {}
    for fruit in fruit_list:
        if not isinstance(fruit, str) or len(fruit.strip()) == 0:
            continue
        key = fruit.lower().strip()
        counts[key] = counts.get(key, 0) + 1
    return counts
if __name__ == '__main__':
    sample_fruits = ["apple", "Banana", "cherry", "APPLE", "", "banana"]
    result = count_fruits(sample_fruits)
    print(result)