class Triangle:
    def __init__(self, sides):
        self.sides = {key: value for key, value in zip(['side1', 'side2', 'side3'], sides)}
    
    def perimeter(self):
        return sum(self.sides.values())

if __name__ == '__main__':
    side_lengths = {'side1': 6, 'side2': 8, 'side3': 10}
    triangle = Triangle(list(side_lengths.values()))
    print(triangle.perimeter())