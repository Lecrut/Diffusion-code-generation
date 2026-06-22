def validate_input(data):
    if not isinstance(data, tuple):
        raise ValueError("Input must be a tuple of strings")

def print_items_separately(iterable):
    for item in iterable:
        print(item)

if __name__ == '__main__':
    data1 = ('apple', 'banana', 'cherry')
    validate_input(data1)
    print_items_separately(data1)
    
    data2 = ()
    validate_input(data2)
    print_items_separately(data2)