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
    print("\n--- Test Case 1: Valid Change ---")
    result1 = date1.set_month_day(11, 30)
    print(f"Set to Month 11, Day 30: {result1}")
    print(f"Date 1 after change: {date1.year}-{date1.month}-{date1.day}")
    print("\n--- Test Case 2: Invalid Day (31 in April) ---")
    date2 = Date(2023, 4, 1)
    result2 = date2.set_month_day(4, 31)
    print(f"Set to Month 4, Day 31: {result2}")
    print(f"Date 2 after change: {date2.year}-{date2.month}-{date2.day}")
    print("\n--- Test Case 3: Leap Year Validation (Feb 29) ---")
    date3 = Date(2024, 2, 1)
    result3 = date3.set_month_day(2, 29)
    print(f"Set to Month 2, Day 29 (Leap Year): {result3}")
    print(f"Date 3 after change: {date3.year}-{date3.month}-{date3.day}")
    print("\n--- Test Case 4: Non-existent Month ---")
    date4 = Date(2023, 1, 1)
    result4 = date4.set_month_day(13, 1)
    print(f"Set to Month 13, Day 1: {result4}")
    print(f"Date 4 after change: {date4.year}-{date4.month}-{date4.day}")
    print("\n--- Test Case 5: Invalid Day (Feb 29 in Non-Leap Year) ---")
    date5 = Date(2023, 2, 1)
    result5 = date5.set_month_day(2, 29)
    print(f"Set to Month 2, Day 29 (Non-Leap Year): {result5}")
    print(f"Date 5 after change: {date5.year}-{date5.month}-{date5.day}")
    print("\n--- Test Case 6: Valid Day (Feb 28 in Non-Leap Year) ---")
    date6 = Date(2023, 2, 1)
    result6 = date6.set_month_day(2, 28)
    print(f"Set to Month 2, Day 28 (Non-Leap Year): {result6}")
    print(f"Date 6 after change: {date6.year}-{date6.month}-{date6.day}")