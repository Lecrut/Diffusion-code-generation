def get_first_and_last(sequence):
    if not sequence:
        raise IndexError("Cannot get first and last elements of an empty sequence.")
    first_element = sequence[0]
    last_element = sequence[-1]
    return (first_element, last_element)
if __name__ == '__main__':
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (5, 15, 25, 35, 45)
    empty_sample = []
    single_sample = [99]
    print(f"List sample: {list_sample}")
    result_list = get_first_and_last(list_sample)
    print(f"First and last of list: {result_list}")
    print(f"\nTuple sample: {tuple_sample}")
    result_tuple = get_first_and_last(tuple_sample)
    print(f"First and last of tuple: {result_tuple}")
    print(f"\nEmpty list sample: {empty_sample}")
    try:
        get_first_and_last(empty_sample)
    except IndexError as e:
        print(f"Caught expected error for empty list: {e}")
    print(f"\nSingle element list sample: {single_sample}")
    result_single = get_first_and_last(single_sample)
    print(f"First and last of single element list: {result_single}")