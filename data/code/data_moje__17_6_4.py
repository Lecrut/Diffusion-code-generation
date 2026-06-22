def get_last_element(data_list):
    if not data_list:
        raise ValueError("The provided list is empty.")
    return data_list[-1]

if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    sample_strings = ["apple", "banana", "cherry", "date"]
    result_numbers = get_last_element(sample_numbers)
    result_strings = get_last_element(sample_strings)
    print(result_numbers)
    print(result_strings)