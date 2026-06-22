from datetime import date, timedelta

class DateSpanCalculator:
    def __init__(self, start: date, end: date):
        self.start = start
        self.end = end

    def calculate_signed_delta(self) -> int:
        return (self.end - self.start).days

    def calculate_absolute_delta(self) -> int:
        return abs(self.calculate_signed_delta())

    def get_date_range(self) -> list:
        count = self.calculate_absolute_delta()
        current = self.start
        if self.calculate_signed_delta() < 0:
            current = self.end
        return [current + timedelta(days=i) for i in range(count + 1)]

if __name__ == '__main__':
    base_date = date(2023, 11, 1)
    target_date = date(2023, 12, 15)
    calculator = DateSpanCalculator(base_date, target_date)
    signed_result = calculator.calculate_signed_delta()
    absolute_result = calculator.calculate_absolute_delta()
    print(signed_result)
    print(absolute_result)
    date_list = calculator.get_date_range()
    print(date_list[0])
    print(date_list[-1])