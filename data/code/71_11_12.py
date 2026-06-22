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
    sample_list = [1, 3, 5, 7, 9]
    result = analyzer.get_middle_value(sample_list)
    print(result)
    sample_list_even = [1, 3, 5, 7]
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_even)