class AreaCalculator:
    def get_difference(self, area_a, area_b):
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    areas = {
        'room': 20.5,
        'garden': 15.3
    }
    difference = calculator.get_difference(areas['room'], areas['garden'])
    print(f"The positive difference is: {difference:.2f}")