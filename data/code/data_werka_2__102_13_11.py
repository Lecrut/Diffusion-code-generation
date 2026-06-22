from datetime import date

class DateValidator:
    def __init__(self, d: date):
        self.d = d

    def is_weekday(self) -> bool:
        return self.d.isoweekday() < 6

if __name__ == '__main__':
    checker = DateValidator(date(2023, 10, 23))
    print(checker.is_weekday())
    print(checker.d.isoweekday())