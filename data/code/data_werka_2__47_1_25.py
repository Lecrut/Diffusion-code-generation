class Triangle:
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
        if self.base < 0 or self.height < 0:
            raise ValueError("Base and height must be non-negative")
    
    def get_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    sample_values = {
        'triangle1': {'base': 3, 'height': 4},
        'triangle2': {'base': 6, 'height': 8},
        'triangle3': {'base': 7.5, 'height': 10}
    }
    
    for name, dimensions in sample_values.items():
        try:
            triangle = Triangle(dimensions['base'], dimensions['height'])
            print(f"{name} area: {triangle.get_area()}")
        except ValueError as e:
            print(f"Error creating {name}: {e}")