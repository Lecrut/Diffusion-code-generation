def count_fruits(fruit_list):
    fruit_counts = {}
    for item in fruit_list:
        if isinstance(item, str) and len(item.strip()) > 0:
            counts = fruit_counts.get(item.lower(), 0)
            fruit_counts[item.lower()] = counts + 1
    return fruit_counts
if __name__ == '__main__':
    sample_fruits = ["apple", "banana", "Apple", "cherry", "date"]
    result = count_fruits(sample_fruits)
    print(result)