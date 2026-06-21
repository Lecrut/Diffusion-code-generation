class DayOfWeekCalculator:
    DAYS_PER_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @classmethod
    def get_days_in_month(cls, year, month):
        if month == 2 and cls.is_leap_year(year):
            return 29
        return cls.DAYS_PER_MONTH[month]

    def calculate_day_of_week(self, date_string):
        parts = date_string.split("-")
        if len(parts) != 3:
            raise ValueError("Invalid date format")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        
        max_days = self.get_days_in_month(year, month)
        if day < 1 or day > max_days:
            raise ValueError("Invalid day")

        total_days = 0
        for y in range(1, year):
            if self.is_leap_year(y):
                total_days += 366
            else:
                total_days += 365
        
        for m in range(1, month):
            total_days += self.get_days_in_month(year, m)
        
        total_days += day
        
        return (total_days - 1) % 7

if __name__ == '__main__':
    calculator = DayOfWeekCalculator()
    print(calculator.calculate_day_of_week("2023-10-23"))
    print(calculator.calculate_day_of_week("2024-01-01"))
    print(calculator.calculate_day_of_week("2000-02-29"))