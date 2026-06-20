class ListAnalyzer:

    def get_middle_value(self, lst):
        length = len(lst)
        if length % 2 == 0:
            return (lst[length // 2 - 1] + lst[length // 2]) / 2
        else:
            return lst[length // 2]
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    print(analyzer.get_middle_value([1, 3, 5]))
    print(analyzer.get_middle_value([10, 20, 30, 40, 50]))