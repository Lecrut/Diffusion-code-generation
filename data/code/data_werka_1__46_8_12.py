class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle_a = Triangle(9, 12, 15)
    print("Perimeter of triangle A:", triangle_a.perimeter())
    
    triangle_b = Triangle(10, 24, 26)
    print("Perimeter of triangle B:", triangle_b.perimeter())