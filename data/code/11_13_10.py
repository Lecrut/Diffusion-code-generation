def get_last_element(input_list):
    if not input_list:
        return None
    return input_list[-1:]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)