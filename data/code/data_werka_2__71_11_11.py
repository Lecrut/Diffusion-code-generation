class ListAnalyzer:
    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List must not be empty")
        n = len(lst)
        if n % 2 == 1:
            return lst[n // 2]
        else:
            return (lst[n // 2 - 1] + lst[n // 2]) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [1, 2, 3, 4, 5]
    result = analyzer.get_middle_value(sample_list)
    print(result)
    sample_list_even = [1, 2, 3, 4]
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_even)