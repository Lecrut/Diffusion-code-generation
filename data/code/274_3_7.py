def is_nested_list(item):
    return isinstance(item, list)

def print_item(item):
    print(item)

def process_data(data):
    for item in data:
        if is_nested_list(item):
            process_data(item)
        else:
            print_item(item)

if __name__ == '__main__':
    sample = [1, [2, 3], [4, [5, 6]], 7]
    process_data(sample)