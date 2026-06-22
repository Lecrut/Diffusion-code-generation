def get_final_element(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list")
    if len(data_list) == 0:
        raise ValueError("List must not be empty")
    return data_list[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    result = get_final_element(sample_list)
    print(result)