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
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [1, 3, 5, 7, 9, 11]
    result_odd = analyzer.get_middle_value(sample_list_odd)
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_odd)
    print(result_even)