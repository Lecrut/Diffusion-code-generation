class ElementChecker:
    MIN_LENGTH = 2

    @staticmethod
    def check_first_and_last(sequence):
        if len(sequence) < ElementChecker.MIN_LENGTH:
            raise ValueError("Sequence must contain at least two elements.")
        return (sequence[0], sequence[-1])

if __name__ == '__main__':
    list_sample = [1, 2, 3, 4, 5]
    tuple_sample = (10, 20, 30)
    empty_list = []

    checker = ElementChecker()
    
    print(f"List sample: {list_sample}")
    try:
        first_last_list = checker.check_first_and_last(list_sample)
        print(f"First and last of list: {first_last_list}")
    except ValueError as e:
        print(f"Error for list: {e}")

    print(f"\nTuple sample: {tuple_sample}")
    try:
        result_tuple = checker.check_first_and_last(tuple_sample)
        print(f"First and last of tuple: {result_tuple}")
    except ValueError as e:
        print(f"Error for tuple: {e}")

    print(f"\nEmpty list: {empty_list}")
    try:
        first_last_empty = checker.check_first_and_last(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")