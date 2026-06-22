class ShapeCalculator:
    def calculate_area(self, shape_type, *params):
        if shape_type == 'circle':
            return self.circle_area(*params)
        elif shape_type == 'square':
            return self.square_area(*params)
        elif shape_type == 'rectangle':
            return self.rectangle_area(*params)
        else:
            raise ValueError("Unsupported shape type")

    def circle_area(self, radius):
        return math.pi * radius ** 2

    def square_area(self, side_length):
        return side_length ** 2

    def rectangle_area(self, length, width):
        return length * width

if __name__ == '__main__':
    calculator = ShapeCalculator()
    print(f"Circle area with radius 5: {calculator.calculate_area('circle', 5)}")
    print(f"Square area with side 4: {calculator.calculate_area('square', 4)}")
    print(f"Rectangle area with length 6 and width 3: {calculator.calculate_area('rectangle', 6, 3)}")