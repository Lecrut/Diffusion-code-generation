def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

class SquareAreaCalculator:
    def __init__(self, areas):
        self.areas = areas

    def calculate_sides(self):
        sides = {}
        for description, area in self.areas.items():
            try:
                side_length = find_side_length(area)
                sides[description] = side_length
            except ValueError as e:
                sides[description] = str(e)
        return sides

if __name__ == '__main__':
    sample_areas = {
        "tiny": 4,
        "standard": 36,
        "large": 81
    }
    calculator = SquareAreaCalculator(sample_areas)
    side_lengths = calculator.calculate_sides()
    for description, side_length in side_lengths.items():
        print(f"The side length of the {description} square is {side_length}")