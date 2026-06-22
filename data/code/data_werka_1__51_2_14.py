class Rectangle:
    def __init__(self, dimensions):
        self.length = dimensions['length']
        self.width = dimensions['width']

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def get_dimensions_from_mapping(name):
    dimensions_map = {
        'small': {'length': 3, 'width': 2},
        'medium': {'length': 6, 'width': 4},
        'large': {'length': 9, 'width': 6}
    }
    return dimensions_map.get(name, None)

if __name__ == '__main__':
    rect1 = Rectangle(get_dimensions_from_mapping('small'))
    perimeter1 = rect1.calculate_perimeter()
    print(perimeter1)
    
    rect2 = Rectangle(get_dimensions_from_mapping('medium'))
    perimeter2 = rect2.calculate_perimeter()
    print(perimeter2)