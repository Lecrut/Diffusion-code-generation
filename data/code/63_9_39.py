class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3],
        ['apple', 'banana', 'cherry'],
        [],
        [True, False]
    ]
    
    for index, lst in enumerate(sample_lists):
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of list {index + 1}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"List {index + 1} is empty: {e}")