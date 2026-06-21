if __name__ == '__main__':
    items = ['red', 'blue', 'green', 'blue', 'red', 'red']
    frequency_map = {item: items.count(item) for item in set(items)}
    print(frequency_map)