def negate_boolean_list(lst):
    if not isinstance(lst, list) or len(lst) != 1:
        raise ValueError("Input must be a list containing exactly one boolean value.")
    return not lst[0]

if __name__ == '__main__':
    sample_list = [True]
    result = negate_boolean_list(sample_list)
    print(result)