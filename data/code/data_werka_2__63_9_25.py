class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_lists = {
        'integers': [1, 2, 3, 4],
        'strings': ['apple', 'banana', 'cherry'],
        'booleans': [True, False],
        'empty_list': []
    }
    
    for category, lst in sample_lists.items():
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of {category}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for {category}: {e}")