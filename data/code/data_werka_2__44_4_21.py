def calculate_perimeter(length, width):
    return 2 * (length + width)

def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Invalid input: Length and width must be positive numbers.")

class RectangleProcessor:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def process(self):
        results = []
        for rect in self.rectangles:
            try:
                length, width = rect
                validate_dimensions(length, width)
                perimeter = calculate_perimeter(length, width)
                results.append(perimeter)
            except ValueError as e:
                results.append(str(e))
        return results

if __name__ == '__main__':
    rectangles = [(6, 4), (9, 3), (-2, 5), (10, 1)]
    processor = RectangleProcessor(rectangles)
    for result in processor.process():
        print(result)