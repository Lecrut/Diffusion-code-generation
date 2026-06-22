class Trapezoid:
    def __init__(self, base_a, base_b, height):
        if base_a <= 0 or base_b <= 0 or height <= 0:
            raise ValueError("Base and height values must be positive numbers.")
        self.base_a = float(base_a)
        self.base_b = float(base_b)
        self.height = float(height)

    def get_area(self):
        return 0.5 * (self.base_a + self.base_b) * self.height

if __name__ == '__main__':
    trapezoid_instance = Trapezoid(5, 7, 4)
    print(trapezoid_instance.get_area())
    trapezoid_instance_2 = Trapezoid(10.5, 8.2, 6.3)
    print(trapezoid_instance_2.get_area())