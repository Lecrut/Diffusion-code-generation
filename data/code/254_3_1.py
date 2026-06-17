class ListAnalyzer:
    def get_minimum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = data[0]
        for element in data[1:]:
            if element < minimum:
                minimum = element
        return minimum
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 5, -3]
    list3 = [42]
    list4 = []
    print(f"Minimum of {list1}: {analyzer.get_minimum(list1)}")
    print(f"Minimum of {list2}: {analyzer.get_minimum(list2)}")
    print(f"Minimum of {list3}: {analyzer.get_minimum(list3)}")
    try:
        analyzer.get_minimum(list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")