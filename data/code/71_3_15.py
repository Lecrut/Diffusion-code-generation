class ListAnalyzer:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List must not be empty")
        self.lst = lst

    def get_middle_value(self):
        n = len(self.lst)
        if n % 2 == 1:
            return self.lst[n // 2]
        else:
            mid = n // 2
            return (self.lst[mid - 1] + self.lst[mid]) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_middle_value())
    
    analyzer2 = ListAnalyzer([1, 2, 3, 4])
    print(analyzer2.get_middle_value())