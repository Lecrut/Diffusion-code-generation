class ListAnalyzer:
    def find_middle(self, data):
        n = len(data)
        if n == 0:
            return None
        if n % 2 != 0:
            return data[n // 2]
        else:
            middle1 = data[n // 2 - 1]
            middle2 = data[n // 2]
            return (middle1 + middle2) / 2
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30, 40]
    list3 = [5, 15]
    list4 = [1, 2, 3, 4]
    list5 = []
    print(f"Middle of {list1}: {analyzer.find_middle(list1)}")
    print(f"Middle of {list2}: {analyzer.find_middle(list2)}")
    print(f"Middle of {list3}: {analyzer.find_middle(list3)}")
    print(f"Middle of {list4}: {analyzer.find_middle(list4)}")
    print(f"Middle of {list5}: {analyzer.find_middle(list5)}")