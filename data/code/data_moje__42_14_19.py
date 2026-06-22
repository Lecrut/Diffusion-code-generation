class Ellipse:
    def __init__(self, major_axis, minor_axis):
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def calculate_area(self):
        return 3.141592653589793 * (self.major_axis / 2) * (self.minor_axis / 2)

if __name__ == '__main__':
    test_ellipse = Ellipse(10, 6)
    print(test_ellipse.calculate_area())