class TimeDeltaCalculator:
    def __init__(self, start_epoch, end_epoch):
        if not isinstance(start_epoch, (int, float)):
            raise ValueError("start_epoch must be numeric")
        if not isinstance(end_epoch, (int, float)):
            raise ValueError("end_epoch must be numeric")
        self.start_epoch = start_epoch
        self.end_epoch = end_epoch

    def get_absolute_difference(self):
        return abs(self.end_epoch - self.start_epoch)

    def get_seconds(self):
        return self.get_absolute_difference()

    def get_minutes(self):
        return self.get_absolute_difference() / 60.0

    def get_hours(self):
        return self.get_absolute_difference() / 3600.0

if __name__ == '__main__':
    t1 = 1609459200
    t2 = 1609462800
    calculator = TimeDeltaCalculator(t1, t2)
    print(calculator.get_seconds())
    print(calculator.get_minutes())
    print(calculator.get_hours())