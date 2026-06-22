class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        if self.lst:
            return self.lst[0]
        else:
            return None

if __name__ == '__main__':
    SAMPLE_LIST = [1, 2, 3, 4, 5]
    analyzer = ListAnalyzer(SAMPLE_LIST)
    print(analyzer.find_first_value())