class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        return self.lst[0] if self.lst else None

if __name__ == '__main__':
    sample_values = {
        'list1': [1, 2, 3],
        'list2': [],
        'list3': ['a', 'b', 'c']
    }
    
    for key, value in sample_values.items():
        analyzer = ListAnalyzer(value)
        print(f"First value of {key}: {analyzer.find_first_value()}")