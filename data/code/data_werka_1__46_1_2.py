class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    side_lengths = {'side1': 3, 'side2': 4, 'side3': 5}
    triangle = Triangle(list(side_lengths.values()))
    print(triangle.perimeter())