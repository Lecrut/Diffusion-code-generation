class ListChecker:
    def __init__(self, data):
        self._data = data
    def get_first_and_last(self):
        if not self._data:
            return None, None
        first = self._data[0]
        last = self._data[-1]
        return first, last
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    checker = ListChecker(sample_list)
    first, last = checker.get_first_and_last()
    print(f"First element: {first}")
    print(f"Last element: {last}")
    sample_list_empty = []
    checker_empty = ListChecker(sample_list_empty)
    first_empty, last_empty = checker_empty.get_first_and_last()
    print(f"First element (empty list): {first_empty}")
    print(f"Last element (empty list): {last_empty}")
    sample_list_single = [99]
    checker_single = ListChecker(sample_list_single)
    first_single, last_single = checker_single.get_first_and_last()
    print(f"First element (single element list): {first_single}")
    print(f"Last element (single element list): {last_single}")