from datetime import date

class WeekdayChecker:
    def __init__(self, target_date: date):
        self.target_date = target_date

    def is_weekday(self) -> bool:
        return self.target_date.weekday() in (0, 1, 2, 3, 4)

if __name__ == '__main__':
    checker = WeekdayChecker(date(2023, 10, 23))
    print(checker.is_weekday())
    checker_weekend = WeekdayChecker(date(2023, 10, 21))
    print(checker_weekend.is_weekday())