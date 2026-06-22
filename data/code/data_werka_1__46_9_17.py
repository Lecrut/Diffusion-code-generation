class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.sides = [side_a, side_b, side_c]
        if any(side <= 0 for side in self.sides):
            raise ValueError("All sides must be positive numbers.")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle_sides = [7, 24, 25]
    my_triangle = Triangle(*triangle_sides)
    print(my_triangle.perimeter())