class RangeCalculator:
    def __init__(self, data):
        if not data:
            raise ValueError("Input set cannot be empty")
        self.data = data

    def calculate_range(self):
        minimum = min(self.data)
        maximum = max(self.data)
        return maximum - minimum

if __name__ == '__main__':
    calculator1 = RangeCalculator({1, 5, 2, 8, 3})
    calculator2 = RangeCalculator({10, 4, 7, 1, 9})
    calculator3 = RangeCalculator(set())
    calculator4 = RangeCalculator({5})

    print(f"Range of {calculator1.data}: {calculator1.calculate_range()}")
    print(f"Range of {calculator2.data}: {calculator2.calculate_range()}")
    try:
        print(f"Range of {calculator3.data}: {calculator3.calculate_range()}")
    except ValueError as e:
        print(f"Error for {calculator3.data}: {e}")
    print(f"Range of {calculator4.data}: {calculator4.calculate_range()}")