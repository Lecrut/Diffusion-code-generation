INDEXED_LIST = ['apple', 'banana', 'cherry']

def print_indexed_items(items):
    for index, item in enumerate(items):
        print(f"{index}: {item}")

if __name__ == '__main__':
    print_indexed_items(INDEXED_LIST)