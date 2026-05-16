class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    def get_middle_value(self):
        n = len(self.data)
        if n == 0:
            return None
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return self.data[n // 2 - 1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    analyzer1 = ListAnalyzer(list1)
    print(analyzer1.get_middle_value())
    list2 = [10, 20, 30, 40]
    analyzer2 = ListAnalyzer(list2)
    print(analyzer2.get_middle_value())
    list3 = [5]
    analyzer3 = ListAnalyzer(list3)
    print(analyzer3.get_middle_value())
    list4 = []
    analyzer4 = ListAnalyzer(list4)
    print(analyzer4.get_middle_value())
    list5 = [1, 2]
    analyzer5 = ListAnalyzer(list5)
    print(analyzer5.get_middle_value())