def get_last_item(data_list):
    if not data_list:
        raise ValueError("The list cannot be empty.")
    return data_list[-1]

if __name__ == '__main__':
    sample_data = [10, 25, 42, 7, 99]
    result = get_last_item(sample_data)
    print(result)