class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def set_month_day(self, new_month, new_day):
        try:
            new_month = int(new_month)
            new_day = int(new_day)
        except ValueError:
            return False
        if new_month < 1 or new_month > 12:
            return False
        if new_day < 1:
            return False
        import calendar
        year = self.year
        month = new_month
        day = new_day
        days_in_month = calendar.monthrange(year, month)[1]
        if new_day > days_in_month:
            return False
        self.month = new_month
        self.day = new_day
        return True
if __name__ == '__main__':
    date1 = Date(2023, 10, 15)
    print(f"Original Date 1: {date1.year}-{date1.month}-{date1.day}")
    print("\nAttempting to set to valid date (2023-10-25):")
    result1 = date1.set_month_day("10", "25")
    print(f"Success: {result1}")
    print(f"New Date 1: {date1.year}-{date1.month}-{date1.day}")
    date2 = Date(2024, 2, 29)
    print(f"\nOriginal Date 2: {date2.year}-{date2.month}-{date2.day}")
    print("\nAttempting to set to valid leap day (2024-02-29):")
    result2 = date2.set_month_day("2", "29")
    print(f"Success: {result2}")
    print(f"New Date 2: {date2.year}-{date2.month}-{date2.day}")
    print("\nAttempting to set to invalid day (2023-02-30):")
    result3 = date1.set_month_day("2", "30")
    print(f"Success: {result3}")
    print(f"Date 1 remains: {date1.year}-{date1.month}-{date1.day}")
    print("\nAttempting to set to invalid month (13):")
    result4 = date1.set_month_day("13", "1")
    print(f"Success: {result4}")
    print(f"Date 1 remains: {date1.year}-{date1.month}-{date1.day}")
    print("\nAttempting to set to invalid day (0):")
    result5 = date1.set_month_day("10", "0")
    print(f"Success: {result5}")
    print(f"Date 1 remains: {date1.year}-{date1.month}-{date1.day}")