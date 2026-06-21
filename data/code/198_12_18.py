class NumericAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_smallest_value(self):
        smallest = float('inf')
        found_any = False
        for sublist in self.data:
            if sublist:
                current_min = min(sublist)
                if current_min < smallest:
                    smallest = current_min
                found_any = True
        return smallest if found_any else None

if __name__ == '__main__':
    analyzer1 = NumericAnalyzer([[-5, 2], [10, -8]])
    print(analyzer1.find_smallest_value())

    analyzer2 = NumericAnalyzer([[3, 7], [-1, 9], [100]])
    print(analyzer2.find_smallest_value())

    analyzer3 = NumericAnalyzer([[1, 2, 3], [], [-5, -10]])
    print(analyzer3.find_smallest_value())

    analyzer4 = NumericAnalyzer([[10], [20], []])
    print(analyzer4.find_smallest_value())