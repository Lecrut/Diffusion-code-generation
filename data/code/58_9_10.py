def validate_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if not lst:
        return False
    return True

def get_first_element(lst):
    if not validate_list(lst):
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45]
    empty_list = []
    first_element = get_first_element(sample_list)
    print(first_element)
    first_empty = get_first_element(empty_list)
    print(first_empty)