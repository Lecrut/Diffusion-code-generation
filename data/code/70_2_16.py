class ListChecker:
    def get_extremes(self, data_list):
        if not isinstance(data_list, list) or len(data_list) < 1:
            raise ValueError("Input must be a non-empty list")
        return (data_list[0], data_list[-1])

if __name__ == '__main__':
    checker = ListChecker()
    sample_list_one = [1, 5, 2, 8, 3]
    sample_list_two = ['a', 'b', 'c', 'd']
    try:
        result_one = checker.get_extremes(sample_list_one)
        print(f"Extremes of {sample_list_one}: {result_one}")
    except ValueError as e:
        print(e)

    try:
        result_two = checker.get_extremes(sample_list_two)
        print(f"Extremes of {sample_list_two}: {result_two}")
    except ValueError as e:
        print(e)

    sample_list_empty = []
    try:
        result_empty = checker.get_extremes(sample_list_empty)
        print(f"Extremes of {sample_list_empty}: {result_empty}")
    except ValueError as e:
        print(e)