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
    print("--- Comparing adjacent elements ---")
    index1 = 0
    result_lt = comparator.compare(sample_list, index1, 'less_than')
    result_gt = comparator.compare(sample_list, index1, 'greater_than')
    result_eq = comparator.compare(sample_list, index1, 'equal')
    print(f"Comparing elements at indices {index1} and {index1 + 1} ({sample_list[index1]} and {sample_list[index1 + 1]}):")
    print(f"Less than: {result_lt}")
    print(f"Greater than: {result_gt}")
    print(f"Equal: {result_eq}")
    print("\n--- Another test case ---")
    index2 = 2
    result_lt = comparator.compare(sample_list, index2, 'less_than')
    result_gt = comparator.compare(sample_list, index2, 'greater_than')
    result_eq = comparator.compare(sample_list, index2, 'equal')
    print(f"Comparing elements at indices {index2} and {index2 + 1} ({sample_list[index2]} and {sample_list[index2 + 1]}):")
    print(f"Less than: {result_lt}")
    print(f"Greater than: {result_gt}")
    print(f"Equal: {result_eq}")
    print("\n--- Edge case test (last element) ---")
    index3 = 3
    result_lt = comparator.compare(sample_list, index3, 'less_than')
    result_gt = comparator.compare(sample_list, index3, 'greater_than')
    result_eq = comparator.compare(sample_list, index3, 'equal')
    print(f"Comparing elements at indices {index3} and {index3 + 1} ({sample_list[index3]} and {sample_list[index3 + 1]}):")
    print(f"Less than: {result_lt}")
    print(f"Greater than: {result_gt}")
    print(f"Equal: {result_eq}")
    print("\n--- Invalid operation test ---")
    try:
        comparator.compare(sample_list, 0, 'unknown')
    except ValueError as e:
        print(f"Caught expected error: {e}")