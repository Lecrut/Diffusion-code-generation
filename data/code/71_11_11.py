class ListAnalyzer:
    def get_middle_value(self, lst):
        if not lst:
            raise ValueError("List is empty")
        length = len(lst)
        mid_index = (length - 1) // 2
        return lst[mid_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [1, 2, 3, 4, 5]
    print(analyzer.get_middle_value(sample_list))