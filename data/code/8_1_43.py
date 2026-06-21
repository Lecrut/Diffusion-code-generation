import numpy as np

class BoundingBoxCalculator:
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError('The list of coordinates cannot be empty.')
        self.coordinates = np.array(coordinates)
    
    def get_min_max(self, axis):
        return (np.min(self.coordinates[:, axis]), np.max(self.coordinates[:, axis]))
    
    def calculate_area(self):
        min_x, max_x = self.get_min_max(0)
        min_y, max_y = self.get_min_max(1)
        width = max_x - min_x
        height = max_y - min_y
        if width < 0 or height < 0:
            raise ValueError('Invalid coordinates: bounding box dimensions cannot be negative.')
        return width * height

if __name__ == '__main__':
    sample_coordinates = [(2, 3), (5, 7), (1, 4), (6, 8)]
    calculator = BoundingBoxCalculator(sample_coordinates)
    area = calculator.calculate_area()
    print(area)