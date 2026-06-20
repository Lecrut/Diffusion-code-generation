class ListAnalyzer:
    def get_middle_value(self, data):
        n = len(data)
        if n == 0:
            return None
        middle_index = n // 2
        return data[middle_index]

if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40, 50, 60]
    list3 = [1, 2, 3, 4]
    list4 = []
    list5 = [5.5, 6.5]

    print(f"Middle of {list1}: {analyzer.get_middle_value(list1)}")
    print(f"Middle of {list2}: {analyzer.get_middle_value(list2)}")
    print(f"Middle of {list3}: {analyzer.get_middle_value(list3)}")
    print(f"Middle of {list4}: {analyzer.get_middle_value(list4)}")
    print(f"Middle of {list5}: {analyzer.get_middle_value(list5)}")