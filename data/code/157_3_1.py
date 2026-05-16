class ListAnalyzer:
    def get_minimum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        minimum = data[0]
        for item in data[1:]:
            if item < minimum:
                minimum = item
        return minimum
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 50, -5]
    list3 = [33, 11, 44, 22]
    empty_list = []
    print(f"Minimum of {list1}: {analyzer.get_minimum(list1)}")
    print(f"Minimum of {list2}: {analyzer.get_minimum(list2)}")
    print(f"Minimum of {list3}: {analyzer.get_minimum(list3)}")
    try:
        analyzer.get_minimum(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")