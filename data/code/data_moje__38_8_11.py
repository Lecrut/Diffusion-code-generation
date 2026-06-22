import math

class ConeVolumeCalculator:
    RADIUS = 8
    HEIGHT = 11
    
    def get_radius(self):
        return self.RADIUS
        
    def get_height(self):
        return self.HEIGHT
        
    def compute_base_area(self):
        return math.pi * self.RADIUS ** 2
        
    def compute_volume(self):
        return self.compute_base_area() * self.HEIGHT / 3
        
    def format_volume(self, value):
        return f"{value:.2f}"

def calculate_cone_volume(radius, height):
    calculator = ConeVolumeCalculator()
    calculator.RADIUS = radius
    calculator.HEIGHT = height
    return calculator.compute_volume()

if __name__ == '__main__':
    calculator = ConeVolumeCalculator()
    print(calculator.get_radius())
    print(calculator.get_height())
    volume = calculate_cone_volume(8, 11)
    print(calculator.format_volume(volume))