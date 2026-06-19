class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print("Perimeter of triangle1:", triangle1.perimeter())

    triangle2 = Triangle(6, 8, 10)
    print("Perimeter of triangle2:", triangle2.perimeter())