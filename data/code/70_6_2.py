def get_first_and_last(sequence):
    if not sequence:
        raise IndexError("Cannot get first and last element of an empty sequence.")
    first_element = sequence[0]
    last_element = sequence[-1]
    return (first_element, last_element)
if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (1, 2, 3, 4, 5)
    single_element = (99,)
    empty_sample = []
    print(f"List sample: {list_sample}")
    try:
        result_list = get_first_and_last(list_sample)
        print(f"First and last of list: {result_list}")
    except IndexError as e:
        print(f"Error for list: {e}")
    print(f"\nTuple sample: {tuple_sample}")
    try:
        result_tuple = get_first_and_last(tuple_sample)
        print(f"First and last of tuple: {result_tuple}")
    except IndexError as e:
        print(f"Error for tuple: {e}")
    print(f"\nSingle element sample: {single_element}")
    try:
        result_single = get_first_and_last(single_element)
        print(f"First and last of single element: {result_single}")
    except IndexError as e:
        print(f"Error for single element: {e}")
    print(f"\nEmpty sample: {empty_sample}")
    try:
        result_empty = get_first_and_last(empty_sample)
        print(f"First and last of empty sequence: {result_empty}")
    except IndexError as e:
        print(f"Error for empty sequence: {e}")