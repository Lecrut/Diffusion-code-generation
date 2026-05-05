def get_first_and_last(sequence):
    if not sequence:
        raise IndexError("Cannot get first and last elements of an empty sequence.")
    first_element = sequence[0]
    last_element = sequence[-1]
    return (first_element, last_element)
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    tuple2 = (10, 20, 30)
    string_seq = "abc"
    empty_list = []
    print(f"List: {list1}")
    try:
        result1 = get_first_and_last(list1)
        print(f"First and Last of {list1}: {result1}")
    except IndexError as e:
        print(f"Error for list1: {e}")
    print(f"\nTuple: {tuple2}")
    try:
        result2 = get_first_and_last(tuple2)
        print(f"First and Last of {tuple2}: {result2}")
    except IndexError as e:
        print(f"Error for tuple2: {e}")
    print(f"\nString: {string_seq}")
    try:
        result3 = get_first_and_last(string_seq)
        print(f"First and Last of {string_seq}: {result3}")
    except IndexError as e:
        print(f"Error for string_seq: {e}")
    print(f"\nEmpty List: {empty_list}")
    try:
        result4 = get_first_and_last(empty_list)
        print(f"First and Last of {empty_list}: {result4}")
    except IndexError as e:
        print(f"Error for empty_list: {e}")