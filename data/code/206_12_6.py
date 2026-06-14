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
    sample_list_1 = [5, 2, 8, 1, 9]
    analyzer1 = ListAnalyzer(sample_list_1)
    print(f"Minimum of {sample_list_1}: {analyzer1.get_minimum()}")
    sample_list_2 = [-10, 0, -5, 3]
    analyzer2 = ListAnalyzer(sample_list_2)
    print(f"Minimum of {sample_list_2}: {analyzer2.get_minimum()}")
    sample_list_3 = [42]
    analyzer3 = ListAnalyzer(sample_list_3)
    print(f"Minimum of {sample_list_3}: {analyzer3.get_minimum()}")
    sample_list_4 = []
    try:
        analyzer4 = ListAnalyzer(sample_list_4)
        analyzer4.get_minimum()
    except ValueError as e:
        print(f"Error for empty list: {e}")