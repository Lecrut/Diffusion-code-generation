import math

def calculate_area_rectangle(length, width):
    return length * width

def calculate_area_circle(radius):
    return math.pi * radius ** 2

class AreaComparator:
    def __init__(self, length, width, radius):
        self.length = length
        self.width = width
        self.radius = radius

    def compare(self):
        rectangle_area = calculate_area_rectangle(self.length, self.width)
        circle_area = calculate_area_circle(self.radius)
        return f"Rectangle Area: {rectangle_area:.2f}, Circle Area: {circle_area:.2f}"

if __name__ == '__main__':
    length = 7.5
    width = 2.0
    radius = 3.5
    comparator = AreaComparator(length, width, radius)
    print(comparator.compare())