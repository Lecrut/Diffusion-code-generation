class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def process_rectangles(rectangles):
    results = []
    for rect in rectangles:
        try:
            perimeter = Rectangle(*rect).calculate_perimeter()
            results.append(perimeter)
        except ValueError as e:
            results.append(str(e))
    return results

if __name__ == '__main__':
    rectangles = [(5, 3), (7, 2), (-1, 4), (8, 0)]
    for result in process_rectangles(rectangles):
        print(result)