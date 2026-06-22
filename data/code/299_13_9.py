from datetime import date

class DateChecker:
    def __init__(self, year, month, day):
        self.date = date(year, month, day)

    def is_weekend(self):
        return self.date.weekday() >= 5

if __name__ == '__main__':
    checker1 = DateChecker(2023, 10, 21)
    print(checker1.is_weekend())
    
    checker2 = DateChecker(2023, 10, 22)
    print(checker2.is_weekend())