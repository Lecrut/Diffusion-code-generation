def get_first_and_last(sequence):
    if not sequence:
        raise IndexError("Cannot get first and last element of an empty sequence.")
    first_element = sequence[0]
    last_element = sequence[-1]
    return (first_element, last_element)
if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (5, 15, 25, 35, 45)
    single_element = [99]
    empty_list = []
    print(f"List sample: {list_sample}")
    try:
        first_last_list = get_first_and_last(list_sample)
        print(f"First and last of list: {first_last_list}")
    except IndexError as e:
        print(f"Error for list: {e}")
    print(f"\nTuple sample: {tuple_sample}")
    try:
        first_last_tuple = get_first_and_last(tuple_sample)
        print(f"First and last of tuple: {first_last_tuple}")
    except IndexError as e:
        print(f"Error for tuple: {e}")
    print(f"\nSingle element sample: {single_element}")
    try:
        first_last_single = get_first_and_last(single_element)
        print(f"First and last of single element: {first_last_single}")
    except IndexError as e:
        print(f"Error for single element: {e}")
    print(f"\nEmpty list sample: {empty_list}")
    try:
        first_last_empty = get_first_and_last(empty_list)
        print(f"First and last of empty list: {first_last_empty}")
    except IndexError as e:
        print(f"Error for empty list: {e}")