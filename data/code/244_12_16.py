class Shape:
    @staticmethod
    def area(triangle):
        return 0.5 * triangle['base'] * triangle['height']

    @staticmethod
    def area(trapezoid):
        return 0.5 * (trapezoid['base1'] + trapezoid['base2']) * trapezoid['height']

if __name__ == '__main__':
    triangle = {'shape_type': 'triangle', 'base': 3, 'height': 4}
    trapezoid = {'shape_type': 'trapezoid', 'base1': 5, 'base2': 7, 'height': 8}
    print(Shape.area(triangle))
    print(Shape.area(trapezoid))