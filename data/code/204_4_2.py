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
    print(f"Middle of {list1}: {analyzer.get_middle(list1)}")
    list2 = [10, 20, 30]
    print(f"Middle of {list2}: {analyzer.get_middle(list2)}")
    list3 = [5]
    print(f"Middle of {list3}: {analyzer.get_middle(list3)}")
    list4 = [1, 2, 3, 4]
    print(f"Middle of {list4}: {analyzer.get_middle(list4)}")
    try:
        list5 = []
        analyzer.get_middle(list5)
    except ValueError as e:
        print(f"Error for empty list: {e}")