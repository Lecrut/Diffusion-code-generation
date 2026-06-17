class FloatMaxFinder:
    def find_max(self, data: list[float]) -> float:
        if not data:
            raise ValueError("Input list cannot be empty")
        max_val = data[0]
        for x in data[1:]:
            if x > max_val:
                max_val = x
        return max_val
if __name__ == '__main__':
    finder = FloatMaxFinder()
    sample_list_1 = [3.14, 1.618, 2.718, 0.577]
    sample_list_2 = [-10.5, -5.2, -20.8, -1.1]
    sample_list_3 = [42.0, 1.0, 99.99, 50.0]
    empty_list = []
    result_1 = finder.find_max(sample_list_1)
    print(f"Max of {sample_list_1}: {result_1}")
    result_2 = finder.find_max(sample_list_2)
    print(f"Max of {sample_list_2}: {result_2}")
    result_3 = finder.find_max(sample_list_3)
    print(f"Max of {sample_list_3}: {result_3}")
    try:
        finder.find_max(empty_list)
    except ValueError as e:
        print(f"Error for empty list: {e}")