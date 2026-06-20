class ElementChecker:
    MIN_SIZE = 2

    @staticmethod
    def check_first_last(sequence):
        if len(sequence) < ElementChecker.MIN_SIZE:
            raise ValueError("Sequence must contain at least two elements.")
        return sequence[0], sequence[-1]

if __name__ == '__main__':
    list_sample = [1, 2, 3, 4, 5]
    tuple_sample = (10, 20, 30)
    single_element = [99]
    empty_list = []

    print(f"List sample: {list_sample}")
    try:
        result_list = ElementChecker.check_first_last(list_sample)
        print(f"First and last of list: {result_list}")
    except ValueError as e:
        print(f"Error for list: {e}")

    print(f"\nTuple sample: {tuple_sample}")
    try:
        result_tuple = ElementChecker.check_first_last(tuple_sample)
        print(f"First and last of tuple: {result_tuple}")
    except ValueError as e:
        print(f"Error for tuple: {e}")

    print(f"\nSingle element list: {single_element}")
    try:
        result_single = ElementChecker.check_first_last(single_element)
        print(f"First and last of single element list: {result_single}")
    except ValueError as e:
        print(f"Error for single element list: {e}")

    print(f"\nEmpty list: {empty_list}")
    try:
        result_empty = ElementChecker.check_first_last(empty_list)
        print(f"First and last of empty list: {result_empty}")
    except ValueError as e:
        print(f"Error for empty list: {e}")