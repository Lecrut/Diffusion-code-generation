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
    sample_values = [
        [100, 200, 300],
        ['x', 'y', 'z'],
        [],
        [True, False, True]
    ]
    
    for index, value_list in enumerate(sample_values):
        try:
            analyzer = ListAnalyzer(value_list)
            print(f"First value of list {index + 1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {index + 1}: {e}")