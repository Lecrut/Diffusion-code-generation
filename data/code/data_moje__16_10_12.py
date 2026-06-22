def get_initial_value(data_list):
    if not data_list:
        return None
    first_element = data_list[0]
    return first_element

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    result = get_initial_value(sample_strings)
    print(result)