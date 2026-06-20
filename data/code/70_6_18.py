class ElementChecker:
    MIN_LENGTH = 2

    @staticmethod
    def check_first_last(sequence):
        if len(sequence) < ElementChecker.MIN_LENGTH:
            raise ValueError("Sequence must contain at least two elements.")
        return sequence[0], sequence[-1]

if __name__ == '__main__':
    checker = ElementChecker()
    list_sample = [10, 20, 30, 40, 50]
    tuple_sample = (5, 15, 25, 35, 45)
    single_element = [99]
    empty_list = []

    try:
        first_last_list = checker.check_first_last(list_sample)
        print(f"First and last of list: {first_last_list}")
    except ValueError as e:
        print(f"Error for list: {e}")

    try:
        result_tuple = checker.check_first_last(tuple_sample)
        print(f"First and Last of tuple: {result_tuple}")
    except ValueError as e:
        print(f"Error for tuple: {e}")

    try:
        checker.check_first_last(single_element)
    except ValueError as e:
        print(f"Error for single element: {e}")

    try:
        checker.check_first_last(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")