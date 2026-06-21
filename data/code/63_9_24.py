class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self._is_list_empty():
            return self.lst[0]
        else:
            raise ValueError("The list is empty")

    def _is_list_empty(self):
        return len(self.lst) == 0

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        ['apple', 'banana', 'cherry'],
        [],
        [True, False]
    ]

    for i, lst in enumerate(sample_lists):
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of list {i+1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {i+1}: {e}")