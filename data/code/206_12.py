class ListAnalyzer:
    def __init__(self, data=None):
        self.data = data
    def get_minimum(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        return min(self.data)
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    analyzer1 = ListAnalyzer(list1)
    print(f"Minimum of {list1}: {analyzer1.get_minimum()}")
    list2 = [-10, 0, 3, -5]
    analyzer2 = ListAnalyzer(list2)
    print(f"Minimum of {list2}: {analyzer2.get_minimum()}")
    list3 = [42]
    analyzer3 = ListAnalyzer(list3)
    print(f"Minimum of {list3}: {analyzer3.get_minimum()}")
    try:
        analyzer4 = ListAnalyzer([])
        analyzer4.get_minimum()
    except ValueError as e:
        print(f"Error for empty list: {e}")