class ListAnalyzer:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        ['apple', 'banana', 'cherry'],
        [],
        [True, False, True]
    ]

    for i, data in enumerate(sample_data):
        try:
            analyzer = ListAnalyzer(data)
            print(f"First value of list {i+1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {i+1}: {e}")