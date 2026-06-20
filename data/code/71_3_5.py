class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def get_middle_value(self):
        length = len(self.lst)
        if length % 2 == 0:
            return (self.lst[length // 2 - 1] + self.lst[length // 2]) / 2
        else:
            return self.lst[length // 2]

if __name__ == '__main__':
    analyzer = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_middle_value())