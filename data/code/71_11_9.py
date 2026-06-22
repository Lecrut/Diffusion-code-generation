class ListAnalyzer:
    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List must not be empty")
        length = len(lst)
        if length % 2 == 0:
            mid_index = length // 2
            return lst[mid_index]
        else:
            mid_index = length // 2
            return lst[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [1, 2, 3, 4, 5]
    result = analyzer.get_middle_value(sample_list)
    print(result)
    sample_list_even = [1, 2, 3, 4]
    result_even = analyzer.get_middle_value(sample_list_even)
    print(result_even)