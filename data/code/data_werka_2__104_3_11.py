from datetime import date

class DateSpan:
    def __init__(self, origin: date, destination: date) -> None:
        self.origin = origin
        self.destination = destination

    def count_days(self) -> int:
        delta = self.destination - self.origin
        return delta.days

    def reversed_count_days(self) -> int:
        return self.count_days() * -1

if __name__ == '__main__':
    start = date(2024, 1, 1)
    end = date(2024, 1, 15)
    span = DateSpan(start, end)
    print(span.count_days())
    print(span.reversed_count_days())