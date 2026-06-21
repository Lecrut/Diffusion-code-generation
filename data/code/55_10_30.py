class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle = Triangle(9, 12, 15)
    print(triangle.perimeter)