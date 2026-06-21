class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    SAMPLE_LISTS = [
        [1, 2, 3, 4, 5],
        ['apple', 'banana', 'cherry'],
        [True, False, True],
        []
    ]

    for i, lst in enumerate(SAMPLE_LISTS):
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of list {i+1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"List {i+1} is empty: {e}")