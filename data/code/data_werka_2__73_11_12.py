class TimeDiffer:
    SECONDS_IN_HOUR = 3600

    def __init__(self, t1, t2):
        self.t1 = float(t1)
        self.t2 = float(t2)

    def calculate_difference(self):
        diff = self.t2 - self.t1
        return diff / self.SECONDS_IN_HOUR

    def get_absolute_difference(self):
        return abs(self.calculate_difference())

    def format_result(self):
        val = self.calculate_difference()
        return f"{val:.2f} hours"

if __name__ == '__main__':
    differ = TimeDiffer(1700000000, 1700007200)
    print(differ.calculate_difference())
    print(differ.get_absolute_difference())
    print(differ.format_result())