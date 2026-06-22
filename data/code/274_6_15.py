sample_items = ['apple', 'banana', 'cherry']

def print_items_with_index(items):
    for index, item in enumerate(items):
        print(f"{index}: {item}")

if __name__ == '__main__':
    print_items_with_index(sample_items)