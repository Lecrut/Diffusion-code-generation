class TimeDeltaCalculator:
    def __init__(self, start_epoch: float, end_epoch: float):
        self.start_epoch = start_epoch
        self.end_epoch = end_epoch

    def calculate_seconds(self) -> float:
        return abs(self.end_epoch - self.start_epoch)

    def calculate_minutes(self) -> float:
        return self.calculate_seconds() / 60.0

if __name__ == '__main__':
    start = 1609459200
    end = 1609462800
    calc = TimeDeltaCalculator(start, end)
    print(calc.calculate_seconds())
    print(calc.calculate_minutes())