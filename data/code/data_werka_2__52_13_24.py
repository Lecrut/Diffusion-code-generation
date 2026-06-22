class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.validate_inputs()
    
    def validate_inputs(self):
        if not (isinstance(self.base, (int, float)) and isinstance(self.height, (int, float))):
            raise ValueError("Base and height must be numbers.")
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def display_area(self):
        area = self.calculate_area()
        print(f"The area of the triangle is: {area}")

if __name__ == '__main__':
    base_value = 20
    height_value = 10
    triangle_instance = Triangle(base_value, height_value)
    triangle_instance.display_area()