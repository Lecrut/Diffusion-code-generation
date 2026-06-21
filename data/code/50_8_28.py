class AreaDifference:
    @staticmethod
    def calculate(area1, area2):
        return abs(area1 - area2)

if __name__ == '__main__':
    result = AreaDifference.calculate(90, 55)
    print(result)