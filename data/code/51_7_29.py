class Shape:
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        total = 0
        for side in self.sides:
            if not isinstance(side, (int, float)):
                raise ValueError("All sides must be numeric")
            total += side
        return total

if __name__ == '__main__':
    sample_sides = [3, 4, 5]
    shape = Shape(sample_sides)
    try:
        print(shape.calculate_perimeter())
    except ValueError as e:
        print(e)

    another_sample_sides = [7, 24, 25]
    another_shape = Shape(another_sample_sides)
    try:
        print(another_shape.calculate_perimeter())
    except ValueError as e:
        print(e)