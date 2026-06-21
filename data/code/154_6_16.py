ITEMS = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

if __name__ == '__main__':
    item_counts = [(item, ITEMS.count(item)) for item in set(ITEMS)]
    print(item_counts)