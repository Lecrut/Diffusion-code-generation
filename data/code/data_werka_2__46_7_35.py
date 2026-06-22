class Triangle:
    def __init__(self, sides):
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive numbers.")
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_triangle = Triangle([3, 4, 5])
    print(sample_triangle.perimeter())