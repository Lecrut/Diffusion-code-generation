def get_last_item(input_list):
    if not input_list:
        raise ValueError("The list is empty")
    return input_list[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))