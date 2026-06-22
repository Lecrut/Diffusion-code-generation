class TrapezoidCalculator:
    TWO = 2.0

    @staticmethod
    def validate_dimensions(base_a, base_b, height):
        if base_a < 0 or base_b < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        return True

    @staticmethod
    def calculate_area(base_a, base_b, height):
        TrapezoidCalculator.validate_dimensions(base_a, base_b, height)
        sum_of_bases = base_a + base_b
        return sum_of_bases * height / TrapezoidCalculator.TWO

if __name__ == '__main__':
    b1 = 8.0
    b2 = 12.0
    h = 5.0
    area_result = TrapezoidCalculator.calculate_area(b1, b2, h)
    print(area_result)