def get_last_item(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if len(input_list) == 0:
        raise ValueError("List cannot be empty")
    return input_list[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)