def validate_list(items):
    if not isinstance(items, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, int) for item in items):
        raise ValueError("All elements in the list must be integers")

def print_first_last(items):
    validate_list(items)
    if len(items) == 1:
        print(items[0])
    elif len(items) > 1:
        print(items[0], items[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print_first_last(sample_list)