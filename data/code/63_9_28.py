class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def validate_list(self):
        if not isinstance(self.lst, list):
            raise ValueError("Input must be a list")
        if not self.lst:
            raise ValueError("The list is empty")

    def find_first_value(self):
        self.validate_list()
        return self.lst[0]

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        ['apple', 'banana', 'cherry'],
        [True, False],
        []
    ]

    for index, value_list in enumerate(sample_values):
        try:
            analyzer = ListAnalyzer(value_list)
            print(f"First value of list {index + 1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {index + 1}: {e}")