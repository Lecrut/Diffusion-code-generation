class AreaDifference:
    def __init__(self, area1, area2):
        self.area1 = area1
        self.area2 = area2

    def get_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    diff_calculator = AreaDifference(90, 45)
    print(diff_calculator.get_difference())