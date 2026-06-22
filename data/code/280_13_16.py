def process_item(item):
    return item * 3

if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    results = [process_item(i) for i in items]
    print(results)