class AreaCalculator:
    def get_difference(self, area_a, area_b):
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    areas = {
        'area1': 30.5,
        'area2': 45.7
    }
    difference = calculator.get_difference(areas['area1'], areas['area2'])
    print(f"The positive difference is: {difference:.2f}")