import calendar

class DateValidator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def validate_day(self):
        return self.day <= calendar.monthrange(self.year, self.month)[1]

if __name__ == '__main__':
    validator = DateValidator(2023, 10, 15)
    is_valid = validator.validate_day()
    print(f"Day {validator.day} of Month {validator.month} in the year {validator.year} is valid: {is_valid}")