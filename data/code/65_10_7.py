def get_sublist(input_list):
    try:
        return input_list[2:5]
    except TypeError as e:
        raise ValueError("Input must be a list") from e

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sublist = get_sublist(sample_list)
    print(sublist)