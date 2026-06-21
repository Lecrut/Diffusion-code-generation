def check_first_and_last(input_list):
    if not isinstance(input_list, (list, tuple)):
        raise TypeError("Input must be a sequence")
    if len(input_list) == 0:
        raise ValueError("Sequence cannot be empty")
    return input_list[0], input_list[-1]

if __name__ == '__main__':
    data = [100, 200, 300, 400]
    result = check_first_and_last(data)
    print(result)