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
            raise ValueError("Invalid operation specified. Use 'less_than', 'greater_than', or 'equal'.")
if __name__ == '__main__':
    comparator = AdjacentComparator()
    sample_list = [10, 20, 5, 30, 15]
    print("Sample List:", sample_list)
    index_to_check = 0
    result_less = comparator.compare(sample_list, index_to_check, 'less_than')
    print(f"Comparing elements at indices {index_to_check} and {index_to_check + 1} (10 vs 20): Less Than? {result_less}")
    index_to_check = 1
    result_greater = comparator.compare(sample_list, index_to_check, 'greater_than')
    print(f"Comparing elements at indices {index_to_check} and {index_to_check + 1} (20 vs 5): Greater Than? {result_greater}")
    index_to_check = 2
    result_equal = comparator.compare(sample_list, index_to_check, 'equal')
    print(f"Comparing elements at indices {index_to_check} and {index_to_check + 1} (5 vs 30): Equal? {result_equal}")
    index_to_check = 3
    result_not_equal = comparator.compare(sample_list, index_to_check, 'equal')
    print(f"Comparing elements at indices {index_to_check} and {index_to_check + 1} (30 vs 15): Equal? {result_not_equal}")
    index_to_check = 4
    print(f"Attempting to compare last two elements (Index {index_to_check} and {index_to_check + 1}): {comparator.compare(sample_list, index_to_check, 'less_than')}")
    try:
        comparator.compare(sample_list, 4, 'unknown_op')
    except ValueError as e:
        print(f"Caught expected error for invalid operation: {e}")