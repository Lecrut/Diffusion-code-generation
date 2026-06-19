class AreaDifferenceCalculator:
    def __init__(self):
        self.differences = []

    def calculate(self, area1, area2):
        difference = abs(area1 - area2)
        self.differences.append(difference)
        return difference

    def get_differences(self):
        return self.differences

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 75
    area_b = 40
    difference_ab = calculator.calculate(area_a, area_b)
    print(f"The difference between {area_a} and {area_b} is: {difference_ab}")
    
    area_c = 200
    area_d = 180
    difference_cd = calculator.calculate(area_c, area_d)
    print(f"The difference between {area_c} and {area_d} is: {difference_cd}")
    
    area_e = 5.678
    area_f = 3.456
    difference_ef = calculator.calculate(area_e, area_f)
    print(f"The difference between {area_e} and {area_f} is: {difference_ef}")
    
    all_differences = calculator.get_differences()
    print("All calculated differences:", all_differences)