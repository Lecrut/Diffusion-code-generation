class RangeCalculator:
    def find_range(self, data):
        if not data:
            return None
        minimum = min(data)
        maximum = max(data)
        return maximum - minimum

if __name__ == '__main__':
    calculator = RangeCalculator()
    sample1 = [1.5, 2.3, 0.8, 4.6, 3.1]
    sample2 = [-5.2, -1.7, -9.3, -2.8, -7.6]
    sample3 = []
    sample4 = [2.7]

    print(f"Range of {sample1}: {calculator.find_range(sample1)}")
    print(f"Range of {sample2}: {calculator.find_range(sample2)}")
    print(f"Range of {sample3}: {calculator.find_range(sample3)}")
    print(f"Range of {sample4}: {calculator.find_range(sample4)}")