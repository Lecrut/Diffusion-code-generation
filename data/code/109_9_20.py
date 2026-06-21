from datetime import date

class MonthCounter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def remaining_days(self):
        delta = self.end - self.start
        return delta.days

    def total_days(self):
        delta = self.end - self.start
        return delta.days + 1

if __name__ == '__main__':
    start = date(2023, 10, 15)
    end = date(2023, 10, 31)
    counter = MonthCounter(start, end)
    print(counter.remaining_days())
    print(counter.total_days())