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
    list1 = [1, 2, 3, 4, 5]
    analyzer1 = ListAnalyzer(list1)
    print(analyzer1.get_middle_value())
    list2 = [10, 20, 30]
    analyzer2 = ListAnalyzer(list2)
    print(analyzer2.get_middle_value())
    list3 = [5]
    analyzer3 = ListAnalyzer(list3)
    print(analyzer3.get_middle_value())
    list4 = []
    analyzer4 = ListAnalyzer(list4)
    print(analyzer4.get_middle_value())
    list5 = [1, 2, 3, 4]
    analyzer5 = ListAnalyzer(list5)
    print(analyzer5.get_middle_value())