class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_middle_value(self):
        n = len(self.data)
        if n == 0:
            return None
        middle_index = n // 2
        return self.data[middle_index]

if __name__ == '__main__':
    sample_list1 = [8, 7, 6, 5, 4, 3, 2, 1]
    analyzer1 = ListAnalyzer(sample_list1)
    print(analyzer1.get_middle_value())

    sample_list2 = [10, 20, 30, 40, 50, 60]
    analyzer2 = ListAnalyzer(sample_list2)
    print(analyzer2.get_middle_value())