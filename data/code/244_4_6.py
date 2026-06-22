import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side_length ** 2

if __name__ == '__main__':
    hex_2 = Hexagon(2)
    hex_3 = Hexagon(3)
    total_area = hex_2.area() + hex_3.area()
    print(f"Area of Hexagon with side length 2: {hex_2.area():.2f}")
    print(f"Area of Hexagon with side length 3: {hex_3.area():.2f}")
    print(f"Total Area: {total_area:.2f}")