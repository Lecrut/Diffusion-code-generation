class Triangle:
    @staticmethod
    def calculate_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {'base': 9, 'height': 4}
    print(Triangle.calculate_area(sample_values['base'], sample_values['height']))