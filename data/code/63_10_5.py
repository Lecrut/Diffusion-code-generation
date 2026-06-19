class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def is_list_empty(self):
        return len(self.lst) == 0

    def find_first_value(self):
        if self.is_list_empty():
            return None
        else:
            return self.lst[0]

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28, 35]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())