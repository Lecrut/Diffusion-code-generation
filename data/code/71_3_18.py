class ListAnalyzer:
    def __init__(self, lst):
        self.lst = lst

    def get_middle_value(self):
        if not self.lst:
            raise ValueError("List must not be empty")
        n = len(self.lst)
        if n % 2 == 1:
            return self.lst[n // 2]
        else:
            mid = n // 2
            return (self.lst[mid - 1] + self.lst[mid]) / 2

if __name__ == '__main__':
    analyzer_odd = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer_odd.get_middle_value())
    analyzer_even = ListAnalyzer([1, 2, 3, 4])
    print(analyzer_even.get_middle_value())