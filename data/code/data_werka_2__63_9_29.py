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
    sample_data = {
        'primes': [2, 3, 5, 7],
        'colors': ['red', 'green', 'blue'],
        'empty_list': []
    }
    
    for category, lst in sample_data.items():
        try:
            analyzer = ListAnalyzer(lst)
            print(f"First value of {category}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"Error for {category}: {e}")