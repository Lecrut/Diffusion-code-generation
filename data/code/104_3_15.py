from datetime import date

class DateSpanCalculator:
    def __init__(self, start: date, end: date):
        self.start = start
        self.end = end

    def calculate_span(self) -> int:
        delta = self.end - self.start
        return delta.days

    def get_start(self) -> date:
        return self.start

    def get_end(self) -> date:
        return self.end

if __name__ == '__main__':
    d1 = date(2024, 1, 1)
    d2 = date(2024, 1, 15)
    calculator = DateSpanCalculator(d1, d2)
    print(calculator.calculate_span())
    print(calculator.get_start())
    print(calculator.get_end())