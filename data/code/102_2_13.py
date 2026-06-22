from datetime import date

class WeekdayChecker:
    _weekdays = range(5)

    def check(self, d: date) -> bool:
        return d.weekday() in self._weekdays

if __name__ == '__main__':
    checker = WeekdayChecker()
    sample = date(2023, 10, 23)
    print(checker.check(sample))
    sample2 = date(2023, 10, 28)
    print(checker.check(sample2))