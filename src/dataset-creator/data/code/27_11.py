def count_fruits(fruit_list):
    fruit_counts = {}
    for fruit in fruit_list:
        if isinstance(fruit, str) and len(fruit.strip()) > 0:
            fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1
    return fruit_counts
if __name__ == '__main__':
    sample_fruits = ['apple', 'banana', 'orange', 'apple', 'grape']
    print(count_fruits(sample_fruits))