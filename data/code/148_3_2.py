class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    def get_largest(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        return max(self.data)
if __name__ == '__main__':
    list1 = [10, 5, 20, 8]
    analyzer1 = ListAnalyzer(list1)
    print(f"Largest in {list1}: {analyzer1.get_largest()}")
    list2 = [-5, -1, -10, -2]
    analyzer2 = ListAnalyzer(list2)
    print(f"Largest in {list2}: {analyzer2.get_largest()}")
    list3 = [3.14, 2.71, 1.618]
    analyzer3 = ListAnalyzer(list3)
    print(f"Largest in {list3}: {analyzer3.get_largest()}")
    list4 = [42]
    analyzer4 = ListAnalyzer(list4)
    print(f"Largest in {list4}: {analyzer4.get_largest()}")
    try:
        analyzer5 = ListAnalyzer([])
        analyzer5.get_largest()
    except ValueError as e:
        print(f"Error for empty list: {e}")