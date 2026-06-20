import math

class Shape:
    def __init__(self, sides):
        self.sides = sides
    
    def perimeter(self):
        return sum(self.sides)
    
    def area(self):
        if len(self.sides) == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        elif len(self.sides) == 4:
            a, b, c, d = self.sides
            if a == b == c == d:
                return a ** 2
            else:
                p = (a + b + c + d) / 2
                return math.sqrt((p - a) * (p - b) * (p - c) * (p - d))
        else:
            raise ValueError("Unsupported number of sides")

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print(f"Perimeter: {triangle.perimeter()}, Area: {triangle.area()}")
    
    square = Shape([5, 5, 5, 5])
    print(f"Perimeter: {square.perimeter()}, Area: {square.area()}")