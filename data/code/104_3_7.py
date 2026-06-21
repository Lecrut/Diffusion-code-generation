from datetime import date

class DateSpanCalculator:
    def __init__(self, start: date, end: date) -> None:
        self.start = start
        self.end = end

    def calculate_net_days(self) -> int:
        delta = self.end - self.start
        return delta.days

    def calculate_absolute_days(self) -> int:
        return abs(self.calculate_net_days())

if __name__ == '__main__':
    reference_start = date(2024, 1, 15)
    reference_end = date(2024, 2, 10)
    calculator = DateSpanCalculator(reference_start, reference_end)
    net_result = calculator.calculate_net_days()
    abs_result = calculator.calculate_absolute_days()
    print(net_result)
    print(abs_result)