class ListAnalyzer:
    def __init__(self):
        pass
    def get_minimum(self, data_list):
        if not data_list:
            raise ValueError("Input list cannot be empty")
        minimum = data_list[0]
        for item in data_list[1:]:
            if item < minimum:
                minimum = item
        return minimum
if __name__ == '__main__':
    analyzer = ListAnalyzer()
    list1 = [5, 2, 8, 1, 9]
    list2 = [-10, 0, 30, -5]
    list3 = [42]
    list4 = []
    print(f"Minimum of {list1}: {analyzer.get_minimum(list1)}")
    print(f"Minimum of {list2}: {analyzer.get_minimum(list2)}")
    print(f"Minimum of {list3}: {analyzer.get_minimum(list3)}")
    try:
        analyzer.get_minimum(list4)
    except ValueError as e:
        print(f"Error for {list4}: {e}")