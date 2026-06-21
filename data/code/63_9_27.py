class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4],
        ['apple', 'banana', 'cherry'],
        [True, False, True],
        []
    ]

    for i, lst in enumerate(sample_lists):
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of list {i + 1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {i + 1}: {e}")