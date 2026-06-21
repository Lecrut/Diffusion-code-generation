if __name__ == '__main__':
    items = ['red', 'blue', 'green', 'red', 'blue', 'blue']
    freq_map = {item: items.count(item) for item in set(items)}
    print(freq_map)