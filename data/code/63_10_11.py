class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if self.lst:
            return self.lst[0]
        else:
            return None

if __name__ == '__main__':
    sample_list = [75, 85, 95, 105, 115]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())