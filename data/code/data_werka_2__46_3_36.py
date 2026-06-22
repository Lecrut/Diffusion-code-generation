class Triangle:
    def __init__(self, sides):
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive integers.")
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle([7, 24, 25])
        print(triangle.perimeter())
        
        another_triangle = Triangle([9, 12, 15])
        print(another_triangle.perimeter())
    except ValueError as e:
        print(e)