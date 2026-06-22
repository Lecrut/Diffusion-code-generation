class RangeCalculator:
    def calculate_range(self, data):
        if not data:
            raise ValueError("Input set cannot be empty")
        return max(data) - min(data)

if __name__ == '__main__':
    calculator = RangeCalculator()
    sample_set1 = {1, 5, 2, 8, 3}
    sample_set2 = {10, 4, 7, 1, 9}
    sample_set3 = set()
    sample_set4 = {5}

    print(f"Range of {sample_set1}: {calculator.calculate_range(sample_set1)}")
    print(f"Range of {sample_set2}: {calculator.calculate_range(sample_set2)}")
    try:
        print(f"Range of {sample_set3}: {calculator.calculate_range(sample_set3)}")
    except ValueError as e:
        print(f"Error for {sample_set3}: {e}")
    print(f"Range of {sample_set4}: {calculator.calculate_range(sample_set4)}")