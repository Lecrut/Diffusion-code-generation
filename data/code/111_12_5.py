class DateManipulator:
    def __init__(self, year, month, day):
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise TypeError("Year, month, and day must be integers.")
        try:
            self._year = year
            self._month = month
            self._day = day
            self._validate_date()
        except ValueError:
            raise ValueError("Invalid date provided.")
    def _validate_date(self):
        if not isinstance(self._year, int) or not isinstance(self._month, int) or not isinstance(self._day, int):
            raise ValueError("Invalid date provided.")
        if not (1 <= self._month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= self._day <= 31):
            raise ValueError("Day must be between 1 and 31.")
        is_leap = (self._year % 4 == 0 and self._year % 100 != 0) or (self._year % 400 == 0)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap:
            max_days = 29
        else:
            max_days = 31
        if self._month == 2 and is_leap:
            max_days = 29
        elif self._month in [4, 6, 9, 11]:
            max_days = 30
        elif self._month == 2:
            max_days = 28
        else:
            max_days = 31
        if self._day > max_days:
            raise ValueError("Day is invalid for the given month and year.")
    def get_year(self):
        return self._year
    def set_year(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError("Year must be an integer.")
        self._year = new_year
        self._validate_date()
    def get_month(self):
        return self._month
    def set_month(self, new_month):
        if not isinstance(new_month, int):
            raise TypeError("Month must be an integer.")
        self._month = new_month
        self._validate_date()
    def get_day(self):
        return self._day
    def set_day(self, new_day):
        if not isinstance(new_day, int):
            raise TypeError("Day must be an integer.")
        self._day = new_day
        self._validate_date()
    def __str__(self):
        return f"{self._year}-{self._month:02d}-{self._day:02d}"
if __name__ == '__main__':
    print("--- Test Case 1: Valid Date (Non-Leap) ---")
    try:
        date1 = DateManipulator(2023, 10, 25)
        print(f"Original: {date1}")
        print(f"Year: {date1.get_year()}, Month: {date1.get_month()}, Day: {date1.get_day()}")
        date1.set_day(31)
        print(f"After setting day to 31: {date1}")
        date1.set_month(12)
        print(f"After setting month to 12: {date1}")
        date1.set_year(2024)
        print(f"After setting year to 2024: {date1}")
    except ValueError as e:
        print(f"Error during test 1: {e}")
    except TypeError as e:
        print(f"Error during test 1: {e}")
    print("\n--- Test Case 2: Leap Year Validation (Feb 29) ---")
    try:
        date2 = DateManipulator(2024, 2, 29)
        print(f"Valid Leap Date: {date2}")
        date2.set_day(30)
        print(f"Attempting invalid day: {date2}")
    except ValueError as e:
        print(f"Caught expected error for invalid day: {e}")
    except TypeError as e:
        print(f"Error during test 2: {e}")
    print("\n--- Test Case 3: Invalid Date Creation (Month Boundary) ---")
    try:
        date3 = DateManipulator(2023, 13, 1)
    except ValueError as e:
        print(f"Caught expected error for invalid month: {e}")
    except TypeError as e:
        print(f"Error during test 3: {e}")
    print("\n--- Test Case 4: Invalid Date Creation (Day Boundary) ---")
    try:
        date4 = DateManipulator(2023, 2, 30)
    except ValueError as e:
        print(f"Caught expected error for invalid day: {e}")
    except TypeError as e:
        print(f"Error during test 4: {e}")
    print("\n--- Test Case 5: Invalid Date Creation (Leap Year Check) ---")
    try:
        date5 = DateManipulator(2023, 2, 29)
    except ValueError as e:
        print(f"Caught expected error for non-leap year Feb 29: {e}")
    except TypeError as e:
        print(f"Error during test 5: {e}")