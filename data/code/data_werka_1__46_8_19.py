class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle1 = Triangle(9, 12, 15)
    print(triangle1.perimeter())
    
    triangle2 = Triangle(5, 7, 9)
    print(triangle2.perimeter())
    
    triangle3 = Triangle(8, 15, 17)
    print(triangle3.perimeter())