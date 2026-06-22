class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst
    
    def find_first_value(self):
        first_element = None
        if self.lst:
            first_element = self.lst[0]
        return first_element

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    analyzer_instance = ListAnalyzer(sample_data)
    result = analyzer_instance.find_first_value()
    print(result)