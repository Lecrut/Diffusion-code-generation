class ListAnalyzer:
    DEFAULT_VALUE = None

    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        return self.lst[0] if self.lst else ListAnalyzer.DEFAULT_VALUE

if __name__ == '__main__':
    sample_list = [90, 190, 290]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())