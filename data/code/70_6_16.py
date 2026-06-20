class ElementChecker:
    def __init__(self, sequence):
        self.sequence = sequence

    def check_first_last(self):
        if len(self.sequence) < 2:
            raise ValueError("Sequence must contain at least two elements.")
        return (self.sequence[0], self.sequence[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    checker = ElementChecker(sample_list)
    try:
        result = checker.check_first_last()
        print(f"First and last of list: {result}")
    except ValueError as e:
        print(f"Error for list: {e}")

    sample_tuple = (10, 20, 30)
    checker_tuple = ElementChecker(sample_tuple)
    try:
        result_tuple = checker_tuple.check_first_last()
        print(f"First and last of tuple: {result_tuple}")
    except ValueError as e:
        print(f"Error for tuple: {e}")