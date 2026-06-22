def negate_boolean_list(lst):
    if not lst:
        raise ValueError("List must contain exactly one element")
    if len(lst) != 1:
        raise ValueError("List must contain exactly one element")
    value = lst[0]
    if not isinstance(value, bool):
        raise ValueError("Element must be a boolean")
    return not value

if __name__ == '__main__':
    sample_list = [True]
    result = negate_boolean_list(sample_list)
    print(result)