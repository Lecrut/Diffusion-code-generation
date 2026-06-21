def negate_boolean_list(lst):
    if len(lst) != 1:
        raise ValueError("List must contain exactly one element")
    if not isinstance(lst[0], bool):
        raise ValueError("Element must be a boolean")
    return not lst[0]

if __name__ == '__main__':
    sample_list = [True]
    result = negate_boolean_list(sample_list)
    print(result)