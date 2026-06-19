def fetch_last_element(array):
    if not isinstance(array, list):
        raise TypeError("Input must be a list")
    if len(array) == 0:
        raise ValueError("Array is empty")
    return array[-1]

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    try:
        print(fetch_last_element(sample_array))
    except (TypeError, ValueError) as e:
        print(e)

    empty_array = []
    try:
        print(fetch_last_element(empty_array))
    except (TypeError, ValueError) as e:
        print(e)

    non_list_input = "not a list"
    try:
        print(fetch_last_element(non_list_input))
    except (TypeError, ValueError) as e:
        print(e)