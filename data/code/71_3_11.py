class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_middle_value(self):
        n = len(self.data)
        if n == 0:
            return None
        mid_index = (n - 1) // 2
        return self.data[mid_index]

if __name__ == '__main__':
    sample_list1 = [3, 5, 2, 8, 1]
    analyzer1 = ListAnalyzer(sample_list1)
    print(analyzer1.get_middle_value())

    sample_list2 = [9, 4, 7, 6, 5, 3]
    analyzer2 = ListAnalyzer(sample_list2)
    print(analyzer2.get_middle_value())