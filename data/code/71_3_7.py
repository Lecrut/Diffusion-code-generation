class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def get_middle_value(self):
        length = len(self.lst)
        if length == 0:
            raise ValueError("List is empty")
        middle_index = length // 2
        return self.lst[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_middle_value())