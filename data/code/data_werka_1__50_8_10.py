class AreaCalculator:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator1 = AreaCalculator(50, 25)
    print(f"The difference between {calculator1.area1} and {calculator1.area2} is: {calculator1.calculate_difference()}")
    
    calculator2 = AreaCalculator(100, 150)
    print(f"The difference between {calculator2.area1} and {calculator2.area2} is: {calculator2.calculate_difference()}")
    
    calculator3 = AreaCalculator(25.5, 15.0)
    print(f"The difference between {calculator3.area1} and {calculator3.area2} is: {calculator3.calculate_difference()}")