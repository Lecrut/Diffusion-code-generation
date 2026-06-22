def validate_list_for_second_to_last(items):
    if not isinstance(items, list):
        raise TypeError("Expected a list")
    if len(items) < 2:
        raise IndexError("List must have at least two elements")

def get_penultimate(lst):
    validate_list_for_second_to_last(lst)
    return lst[-2]

if __name__ == '__main__':
    test_data = [5, 15, 25, 35]
    output = get_penultimate(test_data)
    print(output)