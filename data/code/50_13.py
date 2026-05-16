class AreaCalculator:
    def get_difference(self, area_a, area_b):
        if area_a > area_b:
            return area_a - area_b
        else:
            return area_b - area_a
if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 50
    area2 = 25
    difference = calculator.get_difference(area1, area2)
    print(difference)