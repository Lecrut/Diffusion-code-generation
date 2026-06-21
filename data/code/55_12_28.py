class Triangle:
    def __init__(self, sides):
        if len(sides) != 3:
            raise ValueError("Input must be a tuple of three numbers.")
        self.sides = sides

    def get_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_sides1 = (5, 12, 13)
    triangle1 = Triangle(sample_sides1)
    print(triangle1.get_perimeter())

    sample_sides2 = (8, 15, 17)
    triangle2 = Triangle(sample_sides2)
    print(triangle2.get_perimeter())