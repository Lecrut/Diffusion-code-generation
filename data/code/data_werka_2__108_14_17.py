class DateProcessor:
    def __init__(self, year, month, day):
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise ValueError("Inputs must be integers")
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12")
        if day < 1:
            raise ValueError("Day must be positive")
        
        days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        max_day = days_in_months[month - 1]
        if month == 2 and is_leap:
            max_day = 29
        
        if day > max_day:
            raise ValueError("Day out of range for the given month and year")
        
        self.year = year
        self.month = month
        self.day = day

    def get_day_of_month(self):
        return self.day

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def get_month_name(self):
        names = ("January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December")
        return names[self.month - 1]

if __name__ == '__main__':
    processor = DateProcessor(2024, 2, 29)
    print(processor.get_day_of_month())
    print(processor.is_leap_year())
    print(processor.get_month_name())
    
    processor2 = DateProcessor(2023, 10, 15)
    print(processor2.get_day_of_month())
    print(processor2.is_leap_year())
    print(processor2.get_month_name())