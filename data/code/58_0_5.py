def validate_list(data):
    if not isinstance(data, list) or not data:
        raise ValueError("The provided data is either not a list or is empty.")

def get_first_element(data_list):
    validate_list(data_list)
    return data_list[0]

if __name__ == '__main__':
    sample_list = [99, 88, 77, 66]
    try:
        first_element = get_first_element(sample_list)
        print(first_element)
    except ValueError as e:
        print(e)