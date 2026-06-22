class TimeDeltaCalculator:
    def __init__(self, start_epoch: int, end_epoch: int):
        self.start = start_epoch
        self.end = end_epoch

    def get_absolute_difference(self) -> int:
        return abs(self.end - self.start)

    def get_start_time(self) -> int:
        return self.start

    def get_end_time(self) -> int:
        return self.end

if __name__ == '__main__':
    start_ts = 1609459200
    end_ts = 1609462800
    calculator = TimeDeltaCalculator(start_ts, end_ts)
    diff = calculator.get_absolute_difference()
    print(diff)
    print(calculator.get_start_time())
    print(calculator.get_end_time())