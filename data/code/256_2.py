class RangeCalculator:
    def find_range(self, data):
        if not data:
            return None
        return max(data) - min(data)
if __name__ == '__main__':
    calculator = RangeCalculator()
    sample1 = [1, 5, 2, 8, 3]
    sample2 = [100, 50, 200, 10]
    sample3 = []
    sample4 = [7]
    print(f"Range of {sample1}: {calculator.find_range(sample1)}")
    print(f"Range of {sample2}: {calculator.find_range(sample2)}")
    print(f"Range of {sample3}: {calculator.find_range(sample3)}")
    print(f"Range of {sample4}: {calculator.find_range(sample4)}")