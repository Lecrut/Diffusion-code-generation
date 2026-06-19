class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def find_first_value(self):
        return self.lst[0] if self.lst else None

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())