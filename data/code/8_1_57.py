import numpy as np

class BoundingBoxCalculator:
    def __init__(self, coordinates):
        if not coordinates:
            raise ValueError('The list of coordinates cannot be empty.')
        self.coordinates = np.array(coordinates)
    
    def calculate_min_max(self, axis):
        return np.min(self.coordinates[:, axis]), np.max(self.coordinates[:, axis])
    
    def get_bounding_box_dimensions(self):
        min_x, max_x = self.calculate_min_max(0)
        min_y, max_y = self.calculate_min_max(1)
        width = max_x - min_x
        height = max_y - min_y
        return width, height
    
    def calculate_area(self):
        width, height = self.get_bounding_box_dimensions()
        area = width * height
        return area

if __name__ == '__main__':
    sample_coordinates = [(2, 3), (5, 7), (1, 4), (6, 8)]
    calculator = BoundingBoxCalculator(sample_coordinates)
    print("Width:", calculator.get_bounding_box_dimensions()[0])
    print("Height:", calculator.get_bounding_box_dimensions()[1])
    print("Area:", calculator.calculate_area())