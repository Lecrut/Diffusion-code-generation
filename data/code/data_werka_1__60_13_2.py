def get_last_item(input_list):
    return input_list[-1] if input_list else None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))