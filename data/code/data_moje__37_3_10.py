class ParallelogramCalculator:
    @staticmethod
    def get_area(base, height):
        return float(base * height)

if __name__ == '__main__':
    test_base = 12.5
    test_height = 8.0
    calculated_area = ParallelogramCalculator.get_area(test_base, test_height)
    print(calculated_area)