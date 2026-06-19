def access_first_element(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Input must be a non-empty list')
    return data[0]

def validate_and_access_first_element(data):
    try:
        first_element = access_first_element(data)
        print(f'First element: {first_element}')
        return first_element
    except ValueError as e:
        print(e)
        return None
if __name__ == '__main__':
    int_list = [10, 20, 30]
    string_list = ['apple', 'banana', 'cherry']
    float_list = [3.14, 2.71, 1.618]
    bool_list = [True, False, True]
    empty_list = []
    validate_and_access_first_element(int_list)
    validate_and_access_first_element(string_list)
    validate_and_access_first_element(float_list)
    validate_and_access_first_element(bool_list)
    validate_and_access_first_element(empty_list)