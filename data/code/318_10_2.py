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
        a, b = self.compare_adjacent(data, index)
        if operation == 'less':
            return a < b
        elif operation == 'greater':
            return a > b
        elif operation == 'equal':
            return a == b
        else:
            raise ValueError("Invalid operation specified")
if __name__ == '__main__':
    comparator = AdjacentComparator()
    sample_list = [10, 20, 30, 40, 50]
    print("--- Testing 'less' comparison ---")
    index = 0
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'less')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} < {b} -> {result}")
    index = 2
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'less')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} < {b} -> {result}")
    print("\n--- Testing 'greater' comparison ---")
    index = 3
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'greater')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} > {b} -> {result}")
    print("\n--- Testing 'equal' comparison ---")
    index = 0
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is not None and b is not None:
        result = comparator.compare(sample_list, index, 'equal')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} == {b} -> {result}")
    print("\n--- Testing boundary conditions ---")
    index = 4
    a, b = comparator.compare_adjacent(sample_list, index)
    if a is None:
        print("Index 4 comparison failed (expected None)")
    else:
        result = comparator.compare(sample_list, index, 'less')
        print(f"Comparing {sample_list[index]} and {sample_list[index+1]}: {a} < {b} -> {result}")