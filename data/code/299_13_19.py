from datetime import date

class DateChecker:
    def is_weekend(self, day):
        return day.weekday() >= 5

if __name__ == '__main__':
    checker = DateChecker()
    sample_date1 = date(2023, 10, 21)
    print(checker.is_weekend(sample_date1))
    sample_date2 = date(2023, 10, 22)
    print(checker.is_weekend(sample_date2))