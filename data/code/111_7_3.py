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
        if not (1 <= new_month <= 12):
            return False
        if new_month == 2:
            is_leap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
            if not is_leap:
                if not (1 <= new_day <= 28):
                    return False
                new_day = 28
            elif not (1 <= new_day <= 29):
                return False
        else:
            days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][new_month]
            if not (1 <= new_day <= days_in_month):
                return False
        self.month = new_month
        self.day = new_day
        return True
if __name__ == '__main__':
    date1 = Date(2023, 10, 15)
    print(f"Original Date 1: {date1.year}-{date1.month}-{date1.day}")
    print("\nAttempting to set to valid date (2023-10-20):")
    result1 = date1.set_month_day("10", "20")
    print(f"Result 1: {result1}")
    print(f"New Date 1: {date1.year}-{date1.month}-{date1.day}")
    date2 = Date(2024, 2, 1)
    print(f"\nOriginal Date 2: {date2.year}-{date2.month}-{date2.day}")
    print("\nAttempting to set to valid leap day (2024-2-29):")
    result2 = date2.set_month_day("2", "29")
    print(f"Result 2: {result2}")
    print(f"New Date 2: {date2.year}-{date2.month}-{date2.day}")
    print("\nAttempting to set to invalid day (2023-10-32):")
    result3 = date1.set_month_day("10", "32")
    print(f"Result 3: {result3}")
    print(f"Date 1 remains: {date1.year}-{date1.month}-{date1.day}")
    print("\nAttempting to set to invalid month (13-1):")
    result4 = date1.set_month_day("13", "1")
    print(f"Result 4: {result4}")
    print(f"Date 1 remains: {date1.year}-{date1.month}-{date1.day}")
    date3 = Date(2023, 1, 31)
    print(f"\nOriginal Date 3: {date3.year}-{date3.month}-{date3.day}")
    print("\nAttempting to set to valid 31-day month (2023-01-31):")
    result5 = date3.set_month_day("1", "31")
    print(f"Result 5: {result5}")
    print(f"New Date 3: {date3.year}-{date3.month}-{date3.day}")
    print("\nAttempting to set to invalid day in 30-day month (2023-04-31):")
    result6 = date3.set_month_day("4", "31")
    print(f"Result 6: {result6}")
    print(f"Date 3 remains: {date3.year}-{date3.month}-{date3.day}")