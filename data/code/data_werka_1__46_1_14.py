class Triangle:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    side_lengths = {'a': 6, 'b': 8, 'c': 10}
    triangle = Triangle(list(side_lengths.values()))
    print(triangle.perimeter())