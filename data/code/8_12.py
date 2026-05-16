class GeometryCalculator:
    def calculate_area_of_rectangle(self, length, width):
        return length * width
if __name__ == '__main__':
    calculator = GeometryCalculator()
    length_val = 10
    width_val = 5
    area = calculator.calculate_area_of_rectangle(length_val, width_val)
    print(area)