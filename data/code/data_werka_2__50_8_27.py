class AreaDiff:
    def __init__(self, a1, a2):
        self.diff = abs(a1 - a2)

if __name__ == '__main__':
    diff_calculator = AreaDiff(90, 45)
    print(diff_calculator.diff)