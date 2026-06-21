def validate_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45, 55]
    validate_list(sample_list)
    sublist = sample_list[2:5]
    print(sublist)