class ListAnalyzer:
    EMPTY_LIST_ERROR = "The list is empty"
    
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        self.lst = lst
    
    def find_first_value(self):
        if not self.lst:
            raise ValueError(ListAnalyzer.EMPTY_LIST_ERROR)
        return self.lst[0]

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        ['apple', 'banana', 'cherry'],
        [],
        [None, True, False]
    ]
    
    for index, lst in enumerate(sample_data):
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of list {index + 1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for list {index + 1}: {e}")