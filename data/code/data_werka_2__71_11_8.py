class ListAnalyzer:
    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List must not be empty")
        length = len(lst)
        mid_index = (length - 1) // 2
        return lst[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [10, 20, 30, 40, 50]
    result = analyzer.get_middle_value(sample_list)
    print(result)