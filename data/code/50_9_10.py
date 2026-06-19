class AreaCalculator:
    def get_difference(self, area_a, area_b):
        if not (isinstance(area_a, (int, float)) and isinstance(area_b, (int, float))):
            raise ValueError("Both areas must be numbers.")
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    SAMPLE_AREA_A = 100.5
    SAMPLE_AREA_B = 75.25
    try:
        difference = calculator.get_difference(SAMPLE_AREA_A, SAMPLE_AREA_B)
        print(f"The positive difference is: {difference:.2f}")
    except ValueError as e:
        print(e)