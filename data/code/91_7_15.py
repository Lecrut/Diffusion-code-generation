def invert_boolean_in_list(data):
    if not isinstance(data, list) or len(data) != 1:
        raise ValueError("Input must be a list with exactly one element")
    val = data[0]
    if not isinstance(val, bool):
        raise ValueError("The element must be a boolean")
    return val ^ True

if __name__ == '__main__':
    input_list = [False]
    output = invert_boolean_in_list(input_list)
    print(output)