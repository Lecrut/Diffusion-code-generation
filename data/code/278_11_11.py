def print_items_separately(strings):
    if not all(isinstance(item, str) for item in strings):
        raise ValueError("All items must be strings")
    for item in strings:
        print(item)

if __name__ == '__main__':
    sample_tuple = ('Hello', 'world')
    print_items_separately(sample_tuple)