class Triangle:
    def __init__(self, sides):
        if len(sides) != 3 or not all(isinstance(x, (int, float)) for x in sides):
            raise ValueError("Input must be a tuple of three numbers.")
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_triangle = Triangle((9, 40, 41))
    print(sample_triangle.get_perimeter())