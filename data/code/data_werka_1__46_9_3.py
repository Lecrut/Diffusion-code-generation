class Triangle:
    def __init__(self, sides):
        self.sides = sides
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive numbers.")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle_sides = [6, 8, 10]
    my_triangle = Triangle(triangle_sides)
    print(my_triangle.perimeter())