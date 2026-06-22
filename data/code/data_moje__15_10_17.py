def _validate_list_length(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")

def get_penultimate_element(lst):
    _validate_list_length(lst)
    return lst[-2]

if __name__ == '__main__':
    test_data = ["alpha", "beta", "gamma", "delta"]
    print(get_penultimate_element(test_data))
    short_data = [42]
    try:
        get_penultimate_element(short_data)
    except ValueError as err:
        print(err)