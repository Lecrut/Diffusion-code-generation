import calendar

class DateValidator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_weekday(self):
        try:
            return calendar.weekday(self.year, self.month, self.day) < 5
        except ValueError:
            return False

if __name__ == '__main__':
    validator1 = DateValidator(2023, 10, 23)
    print(validator1.is_weekday())
    validator2 = DateValidator(2023, 10, 28)
    print(validator2.is_weekday())
    validator3 = DateValidator(2023, 2, 29)
    print(validator3.is_weekday())