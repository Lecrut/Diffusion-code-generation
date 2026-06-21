class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def compare_shapes(rectangle, square):
    comparison_result = {
        'rectangle': {
            'area': rectangle.area(),
            'perimeter': rectangle.perimeter()
        },
        'square': {
            'area': square.area(),
            'perimeter': square.perimeter()
        }
    }
    return comparison_result

if __name__ == '__main__':
    side_length = 5
    rectangle_length = 8
    rectangle_width = 6
    
    rectangle = Shape(rectangle_length, rectangle_width)
    square = Shape(side_length)
    
    print(compare_shapes(rectangle, square))