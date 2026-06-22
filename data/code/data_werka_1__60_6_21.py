def validate_list(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if len(input_list) == 0:
        raise ValueError("The list is empty")

def get_last_element(safe_list):
    try:
        validate_list(safe_list)
        return safe_list[-1]
    except (TypeError, ValueError) as e:
        return str(e)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    empty_data = []
    invalid_data = "not a list"

    print("Last element of sample_data:", get_last_element(sample_data))
    print("Attempting to get last element of empty_data:", get_last_element(empty_data))
    print("Attempting to get last element of invalid_data:", get_last_element(invalid_data))