def validate_input(iterable):
    if not isinstance(iterable, tuple) or not all(isinstance(item, str) for item in iterable):
        raise ValueError("Input must be a tuple of strings")

def print_items_separately(iterable):
    validate_input(iterable)
    for item in iterable:
        print(item)

if __name__ == '__main__':
    data1 = ('Hello', 'World')
    data2 = ()
    try:
        print_items_separately(data1)
        print_items_separately(data2)
    except ValueError as e:
        print(e)