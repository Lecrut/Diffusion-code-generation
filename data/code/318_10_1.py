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
    sample_list = [10, 20, 5, 30, 15]
    print("--- Comparing adjacent elements ---")
    index1 = 0
    result_lt = comparator.compare(sample_list, index1, 'less_than')
    result_gt = comparator.compare(sample_list, index1, 'greater_than')
    result_eq = comparator.compare(sample_list, index1, 'equal')
    print(f"Comparing elements at indices {index1} and {index1 + 1}: ({sample_list[index1]}, {sample_list[index1 + 1]})")
    print(f"Is {sample_list[index1]} less than {sample_list[index1 + 1]}? {result_lt}")
    print(f"Is {sample_list[index1]} greater than {sample_list[index1 + 1]}? {result_gt}")
    print(f"Are {sample_list[index1]} equal to {sample_list[index1 + 1]}? {result_eq}")
    print("\n--- Comparing another pair ---")
    index2 = 2
    result_lt = comparator.compare(sample_list, index2, 'less_than')
    result_gt = comparator.compare(sample_list, index2, 'greater_than')
    result_eq = comparator.compare(sample_list, index2, 'equal')
    print(f"Comparing elements at indices {index2} and {index2 + 1}: ({sample_list[index2]}, {sample_list[index2 + 1]})")
    print(f"Is {sample_list[index2]} less than {sample_list[index2 + 1]}? {result_lt}")
    print(f"Is {sample_list[index2]} greater than {sample_list[index2 + 1]}? {result_gt}")
    print(f"Are {sample_list[index2]} equal to {sample_list[index2 + 1]}? {result_eq}")
    print("\n--- Edge case: Last element ---")
    index_last = len(sample_list) - 1
    result_lt = comparator.compare(sample_list, index_last, 'less_than')
    print(f"Comparing elements at indices {index_last} and {index_last + 1}: ({sample_list[index_last]}, N/A)")
    print(f"Is {sample_list[index_last]} less than next element? {result_lt}")