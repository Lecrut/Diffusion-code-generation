class RangeCalculator:
    @staticmethod
    def find_range(data):
        if not data:
            raise ValueError("Input set cannot be empty")
        minimum = min(data)
        maximum = max(data)
        return maximum - minimum

if __name__ == '__main__':
    sample_sets = [
        {1, 5, 2, 8, 3},
        {10, 4, 7, 1, 9},
        set(),
        {5}
    ]
    
    for sample_set in sample_sets:
        try:
            range_result = RangeCalculator.find_range(sample_set)
            print(f"Range of {sample_set}: {range_result}")
        except ValueError as e:
            print(f"Error for {sample_set}: {e}")