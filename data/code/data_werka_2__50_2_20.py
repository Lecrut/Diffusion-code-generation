class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    AREA_THRESHOLD = 50.0
    area_a = 120.0
    area_b = 70.0
    
    calculator = AreaDifferenceCalculator(area_a, area_b)
    difference = calculator.calculate_difference()
    
    if difference > AREA_THRESHOLD:
        print(f"Difference exceeds threshold: {difference}")
    else:
        print(f"Difference within threshold: {difference}")