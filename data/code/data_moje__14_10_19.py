def _validate_has_third(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) < 3:
        raise IndexError("List too short")

def get_third_element(lst):
    _validate_has_third(lst)
    return lst[2]

if __name__ == '__main__':
    sample_values = [100, 200, 300, 400]
    result = get_third_element(sample_values)
    print(result)