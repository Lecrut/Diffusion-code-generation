class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def get_middle_value(self):
        length = len(self.lst)
        mid_index = length // 2
        if length % 2 == 0:
            return (self.lst[mid_index - 1] + self.lst[mid_index]) / 2
        else:
            return self.lst[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer([3, 5, 7, 9, 11])
    print(analyzer.get_middle_value())