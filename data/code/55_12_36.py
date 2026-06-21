class Triangle:
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError("Input must be a tuple of three numbers.")
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides = (5, 12, 13)
    triangle = Triangle(sample_sides)
    print(triangle.get_perimeter())