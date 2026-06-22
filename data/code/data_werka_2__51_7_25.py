class PerimeterCalculator:
    @staticmethod
    def is_numeric(value):
        return isinstance(value, (int, float))

    @classmethod
    def calculate_perimeter(cls, sides):
        if not all(cls.is_numeric(side) for side in sides):
            raise ValueError("All sides must be numeric")
        return sum(sides)

if __name__ == '__main__':
    sample_sides = [8, 15, 17]
    try:
        print(PerimeterCalculator.calculate_perimeter(sample_sides))
    except ValueError as e:
        print(e)