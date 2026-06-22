class AreaCalculator:
    def get_difference(self, area_a, area_b):
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    SAMPLE_AREA_A = 75.25
    SAMPLE_AREA_B = 48.90
    difference = calculator.get_difference(SAMPLE_AREA_A, SAMPLE_AREA_B)
    print(f"The positive difference is: {difference:.2f}")