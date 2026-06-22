class DateProcessor:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_day_of_month(self):
        return self.day

    def is_valid_date(self):
        days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if self.month < 1 or self.month > 12:
            return False
        if self.day < 1:
            return False
        max_day = days_in_months[self.month - 1]
        if self.month == 2:
            is_leap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
            if is_leap:
                max_day = 29
        if self.day > max_day:
            return False
        return True

if __name__ == '__main__':
    processor = DateProcessor(2023, 10, 15)
    print(processor.get_day_of_month())
    print(processor.is_valid_date())
    
    processor2 = DateProcessor(2024, 2, 29)
    print(processor2.get_day_of_month())
    print(processor2.is_valid_date())