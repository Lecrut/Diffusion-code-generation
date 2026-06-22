class ListAnalyzer:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List must not be empty")
        self.lst = lst

    def get_middle_value(self):
        length = len(self.lst)
        middle_index = length // 2
        if length % 2 == 0:
            val1 = self.lst[middle_index - 1]
            val2 = self.lst[middle_index]
            return (val1 + val2) / 2
        else:
            return self.lst[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_middle_value())
    analyzer2 = ListAnalyzer([1, 2, 3, 4])
    print(analyzer2.get_middle_value())