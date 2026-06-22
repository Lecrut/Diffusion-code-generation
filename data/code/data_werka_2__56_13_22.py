class Shape:
    def __init__(self, length, width=None):
        if width is None:
            self.length = self.width = length
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

def compare_shapes():
    rectangle = Shape(5, 3)
    square = Shape(5)
    comparison_result = {
        'rectangle': {'area': rectangle.area(), 'perimeter': rectangle.perimeter()},
        'square': {'area': square.area(), 'perimeter': square.perimeter()}
    }
    return comparison_result

if __name__ == '__main__':
    result = compare_shapes()
    print(result)