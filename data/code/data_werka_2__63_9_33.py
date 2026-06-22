class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if not self.lst:
            raise ValueError("The list is empty")
        return self.lst[0]

if __name__ == '__main__':
    sample_data = {
        'fruits': ['apple', 'banana', 'cherry'],
        'vegetables': ['carrot', 'broccoli', 'spinach'],
        'empty_list': []
    }
    
    for category, items in sample_data.items():
        try:
            analyzer = ListAnalyzer(items)
            print(f"First value of {category}: {analyzer.find_first_value()}")
        except ValueError as e:
            print(f"No first value found for {category}: {e}")