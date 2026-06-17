class AdjacentComparator:
    def compare_adjacent(self, data, index):
        if index + 1 < len(data):
            a = data[index]
            b = data[index + 1]
            return a, b
        return None, None
    def compare(self, data, index, operation):
        if index is None or index + 1 >= len(data):
            return None
        a, b = data[index], data[index + 1]
        if operation == 'less_than':
            return a < b
        elif operation == 'greater_than':
            return a > b
        elif operation == 'equal':
            return a == b
        else:
            raise ValueError("Invalid operation specified. Must be 'less_than', 'greater_than', or 'equal'.")
if __name__ == '__main__':
    comparator = AdjacentComparator()
    sample_list = [10, 20, 30, 40, 50]
    print("--- Testing Less Than ---")
    index = 0
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'less_than')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} < {b} -> {result}")
    index = 2
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'less_than')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} < {b} -> {result}")
    print("\n--- Testing Greater Than ---")
    index = 3
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'greater_than')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} > {b} -> {result}")
    print("\n--- Testing Equal ---")
    index = 0
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'equal')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} == {b} -> {result}")
    print("\n--- Testing Boundary Conditions ---")
    index = len(sample_list) - 1
    a, b = comparator.compare_adjacent(sample_list, index)
    print(f"Comparing last two elements: {a}, {b}")
    index = len(sample_list)
    result = comparator.compare(sample_list, index, 'less_than')
    print(f"Index out of bounds comparison result: {result}")