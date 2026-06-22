def get_third_element(data_list):
    if len(data_list) < 3:
        raise IndexError("List must contain at least three elements.")
    return data_list[2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_third_element(sample_data)
    print(result)