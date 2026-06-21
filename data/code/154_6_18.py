ITEMS = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

if __name__ == '__main__':
    result = [(item, ITEMS.count(item)) for item in set(ITEMS)]
    print(result)