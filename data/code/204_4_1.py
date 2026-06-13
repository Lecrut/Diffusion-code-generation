class ListAnalyzer:
    def __init__(self):
        pass
    def get_middle(self, data):
        n = len(data)
        if n == 0:
            raise ValueError("List cannot be empty")
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 20, 30]
    list3 = [7]
    list4 = []
    print(f"Middle of {list1}: {analyzer.get_middle(list1)}")
    print(f"Middle of {list2}: {analyzer.get_middle(list2)}")
    print(f"Middle of {list3}: {analyzer.get_middle(list3)}")
    try:
        analyzer.get_middle(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")