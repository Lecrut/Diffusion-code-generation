def print_indexed_items(items):
    for index, item in enumerate(items):
        print(f"{index}: {item}")

if __name__ == '__main__':
    sample_items = ['apple', 'banana', 'cherry']
    print_indexed_items(sample_items)