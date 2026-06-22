def print_items_separately(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All elements in the tuple must be strings.")
    for item in items:
        print(item)

if __name__ == '__main__':
    sample_tuple = ('Hello', 'world!', 'This', 'is', 'a', 'test.')
    try:
        print_items_separately(sample_tuple)
    except ValueError as e:
        print(e)