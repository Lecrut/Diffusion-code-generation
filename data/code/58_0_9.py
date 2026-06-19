def validate_list(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if not data_list:
        raise ValueError("The list is empty.")

def access_first_element(data_list):
    validate_list(data_list)
    return data_list[0]

if __name__ == '__main__':
    sample_list = [9, 18, 27, 36]
    first_element = access_first_element(sample_list)
    print(first_element)