ITEMS = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

if __name__ == '__main__':
    frequency_map = {item: ITEMS.count(item) for item in set(ITEMS)}
    print(frequency_map)