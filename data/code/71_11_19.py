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
    sample_list_odd = [10, 20, 30, 40, 50]
    sample_list_even = [10, 20, 30, 40]
    print(analyzer.get_middle_value(sample_list_odd))
    print(analyzer.get_middle_value(sample_list_even))