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
    min1 = analyzer1.get_minimum()
    print(f"Minimum of {sample_list_1} is: {min1}")
    sample_list_2 = [-10, 50, 3, -100, 20]
    analyzer2 = ListAnalyzer(sample_list_2)
    min2 = analyzer2.get_minimum()
    print(f"Minimum of {sample_list_2} is: {min2}")
    sample_list_3 = [42]
    analyzer3 = ListAnalyzer(sample_list_3)
    min3 = analyzer3.get_minimum()
    print(f"Minimum of {sample_list_3} is: {min3}")
    try:
        sample_list_4 = []
        analyzer4 = ListAnalyzer(sample_list_4)
        analyzer4.get_minimum()
    except ValueError as e:
        print(f"Error for empty list: {e}")