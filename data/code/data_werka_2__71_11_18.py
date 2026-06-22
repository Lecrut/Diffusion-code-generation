class ListAnalyzer:
    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List must not be empty")
        n = len(lst)
        if n % 2 == 1:
            return lst[n // 2]
        else:
            mid = n // 2
            return (lst[mid - 1] + lst[mid]) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 2, 3, 4]
    print(analyzer.get_middle_value(odd_list))
    print(analyzer.get_middle_value(even_list))