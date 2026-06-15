class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    def get_middle(self):
        n = len(self.data)
        if n == 0:
            raise ValueError("Cannot find the middle of an empty list")
        middle_index = n // 2
        return self.data[middle_index]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    analyzer1 = ListAnalyzer(list1)
    print(f"Middle of {list1}: {analyzer1.get_middle()}")
    list2 = [10, 20, 30, 40, 50, 60]
    analyzer2 = ListAnalyzer(list2)
    print(f"Middle of {list2}: {analyzer2.get_middle()}")
    list3 = [1, 2, 3, 4]
    analyzer3 = ListAnalyzer(list3)
    print(f"Middle of {list3}: {analyzer3.get_middle()}")
    list4 = [99]
    analyzer4 = ListAnalyzer(list4)
    print(f"Middle of {list4}: {analyzer4.get_middle()}")
    list5 = []
    try:
        analyzer5 = ListAnalyzer(list5)
        analyzer5.get_middle()
    except ValueError as e:
        print(f"Error for empty list: {e}")