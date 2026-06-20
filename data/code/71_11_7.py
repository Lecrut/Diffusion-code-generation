class ListAnalyzer:

    def get_middle_value(self, lst):
        length = len(lst)
        if length % 2 == 0:
            return None
        else:
            return lst[length // 2]
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    sample_list = [1, 2, 3, 4, 5]
    print(analyzer.get_middle_value(sample_list))