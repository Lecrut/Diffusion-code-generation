class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    def get_minimum(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    analyzer1 = ListAnalyzer(list1)
    print(f"Minimum of {list1}: {analyzer1.get_minimum()}")
    list2 = [-10, 0, 5, -3]
    analyzer2 = ListAnalyzer(list2)
    print(f"Minimum of {list2}: {analyzer2.get_minimum()}")
    list3 = [42]
    analyzer3 = ListAnalyzer(list3)
    print(f"Minimum of {list3}: {analyzer3.get_minimum()}")
    list4 = []
    try:
        analyzer4 = ListAnalyzer(list4)
        analyzer4.get_minimum()
    except ValueError as e:
        print(f"Error for empty list: {e}")