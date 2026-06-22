class Rhombus:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def area(self):
        return (self.d1 * self.d2) / 2

def calculate_area_sum(rhombus1, rhombus2):
    return rhombus1.area() + rhombus2.area()

if __name__ == '__main__':
    r1 = Rhombus(6, 8)
    r2 = Rhombus(10, 12)
    result = calculate_area_sum(r1, r2)
    print(result)