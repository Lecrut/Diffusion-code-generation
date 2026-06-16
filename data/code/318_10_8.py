class AdjacentComparator:
    def compare_adjacent(self, data, index):
        if index + 1 < len(data):
            a = data[index]
            b = data[index + 1]
            return a, b
        return None, None
    def compare(self, data, index, operation):
        a, b = self.compare_adjacent(data, index)
        if a is None or b is None:
            return None
        if operation == 'less_than':
            return a < b
        elif operation == 'greater_than':
            return a > b
        elif operation == 'equal':
            return a == b
        else:
            raise ValueError("Invalid operation specified")
if __name__ == '__main__':
    comparator = AdjacentComparator()
    sample_list = [10, 25, 5, 30, 15]
    print("--- Comparing adjacent elements ---")
    index = 0
    result_less = comparator.compare(sample_list, index, 'less_than')
    print(f"Comparing index {index} ({sample_list[index]}) and {index + 1} ({sample_list[index + 1]}): Less Than -> {result_less}")
    index = 1
    result_greater = comparator.compare(sample_list, index, 'greater_than')
    print(f"Comparing index {index} ({sample_list[index]}) and {index + 1} ({sample_list[index + 1]}): Greater Than -> {result_greater}")
    index = 2
    result_equal = comparator.compare(sample_list, index, 'equal')
    print(f"Comparing index {index} ({sample_list[index]}) and {index + 1} ({sample_list[index + 1]}): Equal -> {result_equal}")
    index = 3
    result_unknown = comparator.compare(sample_list, index, 'less_than')
    print(f"Comparing index {index} ({sample_list[index]}) and {index + 1} ({sample_list[index + 1]}): Less Than -> {result_unknown}")
    index = 4
    result_none = comparator.compare(sample_list, index, 'greater_than')
    print(f"Comparing index {index} ({sample_list[index]}) and {index + 1} (Out of bounds): Greater Than -> {result_none}")