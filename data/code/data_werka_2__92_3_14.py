def invert_truth_values(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    if len(input_list) == 0:
        return []
    return [not val for val in input_list]

if __name__ == '__main__':
    data = [True, False, True, False, True]
    output = invert_truth_values(data)
    print(output)