class SquareCalculator:
    @staticmethod
    def get_areas(side_lengths):
        return [length * length for length in side_lengths]

if __name__ == '__main__':
    test_sides = [7, 12, 15, 20, 25]
    output_areas = SquareCalculator.get_areas(test_sides)
    print(output_areas)