class ListAnalyzer:
    def get_middle_value(self, lst):
        length = len(lst)
        if length == 0:
            raise ValueError("List is empty")
        middle_index = length // 2
        return lst[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [1, 2, 3, 4, 5]
    print(analyzer.get_middle_value(sample_list))