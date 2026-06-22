class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_perimeter(self):
        a, b = self.major_axis, self.minor_axis
        h = ((a - b) ** 2) / ((a + b) ** 2)
        return 2 * (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

if __name__ == '__main__':
    ellipse1 = Ellipse(6, 4)
    print(f"Perimeter of ellipse with major axis {ellipse1.major_axis} and minor axis {ellipse1.minor_axis}: {ellipse1.calculate_perimeter()}")
    
    ellipse2 = Ellipse(8, 3)
    print(f"Perimeter of ellipse with major axis {ellipse2.major_axis} and minor axis {ellipse2.minor_axis}: {ellipse2.calculate_perimeter()}")