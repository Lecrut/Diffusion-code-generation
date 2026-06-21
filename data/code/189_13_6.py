def validate_input(lst, value):
    if not isinstance(lst, list):
        raise ValueError("First argument must be a list.")
    if not all(isinstance(item, type(value)) for item in lst):
        raise ValueError("All items in the list must be of the same type as the value to remove.")

def remove_value(lst, value):
    validate_input(lst, value)
    return [x for x in lst if x != value]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    value_to_remove = 3
    result = remove_value(sample_list, value_to_remove)
    print(result)