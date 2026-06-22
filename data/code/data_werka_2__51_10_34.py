class Rectangle:
    def __init__(self, dimensions):
        if dimensions['width'] <= 0 or dimensions['height'] <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = dimensions['width']
        self.height = dimensions['height']
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    sample_dimensions = {'width': 6.0, 'height': 4.0}
    rectangle = Rectangle(sample_dimensions)
    print(rectangle.calculate_perimeter())