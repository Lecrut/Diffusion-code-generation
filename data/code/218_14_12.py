class NestedListMinimizer:
    MIN_VALUE = float('inf')

    @staticmethod
    def flatten_and_find_min(nested_list):
        min_value = NestedListMinimizer.MIN_VALUE
        for sublist in nested_list:
            if sublist:
                current_min = min(sublist)
                if current_min < min_value:
                    min_value = current_min
        return min_value if min_value != NestedListMinimizer.MIN_VALUE else None

if __name__ == '__main__':
    minimizer = NestedListMinimizer()
    test_case_1 = [[1, 5, 3], [8, 2, 9]]
    test_case_2 = [[10, 20], [5, 15]]
    print(f"Test Case 1: {test_case_1} -> Minimum: {minimizer.flatten_and_find_min(test_case_1)}")
    print(f"Test Case 2: {test_case_2} -> Minimum: {minimizer.flatten_and_find_min(test_case_2)}")