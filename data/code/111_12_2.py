class DateManipulator:
    def __init__(self, year, month, day):
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise TypeError("Year, month, and day must be integers.")
        self._year = year
        self._month = month
        self._day = day
        self._validate()
    def _validate(self):
        if not (1 <= self._month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= self._day <= 31):
            raise ValueError("Day must be between 1 and 31.")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self._month == 2:
            is_leap = self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0)
            max_days = 29 if is_leap else 28
        else:
            max_days = days_in_month[self._month]
        if self._day > max_days:
            raise ValueError(f"Day {self._day} is invalid for month {self._month} in year {self._year}.")
    def get_year(self):
        return self._year
    def set_year(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError("Year must be an integer.")
        self._year = new_year
        self._validate()
    def get_month(self):
        return self._month
    def set_month(self, new_month):
        if not isinstance(new_month, int):
            raise TypeError("Month must be an integer.")
        self._month = new_month
        self._validate()
    def get_day(self):
        return self._day
    def set_day(self, new_day):
        if not isinstance(new_day, int):
            raise TypeError("Day must be an integer.")
        self._day = new_day
        self._validate()
    def __str__(self):
        return f"{self._year}-{self._month:02d}-{self._day:02d}"
if __name__ == '__main__':
    print("--- Test Case 1: Valid Date (Non-Leap Year) ---")
    try:
        date1 = DateManipulator(2023, 10, 25)
        print(f"Initial Date: {date1}")
        print(f"Year: {date1.get_year()}, Month: {date1.get_month()}, Day: {date1.get_day()}")
        date1.set_year(2024)
        print(f"After setting year to 2024: {date1}")
        date1.set_day(31)
        print(f"After setting day to 31: {date1}")
    except ValueError as e:
        print(f"Error during operation: {e}")
    except TypeError as e:
        print(f"Error during operation: {e}")
    print("\n--- Test Case 2: Leap Year Validation (February 29th) ---")
    try:
        date2 = DateManipulator(2024, 2, 29)
        print(f"Initial Date: {date2}")
        print(f"Leap Year Check: {date2._year % 4 == 0 and (date2._year % 100 != 0 or date2._year % 400 == 0)}")
        date2.set_day(30)
        print(f"After setting day to 30: {date2}")
    except ValueError as e:
        print(f"Error during operation: {e}")
    print("\n--- Test Case 3: Invalid Date Creation (Month Boundary) ---")
    try:
        DateManipulator(2023, 13, 1)
    except ValueError as e:
        print(f"Successfully caught error for invalid month: {e}")
    print("\n--- Test Case 4: Invalid Date Creation (Day Boundary) ---")
    try:
        DateManipulator(2023, 4, 31)
    except ValueError as e:
        print(f"Successfully caught error for invalid day: {e}")
    print("\n--- Test Case 5: Invalid Date Creation (Leap Year Check - Feb 29th in 2023) ---")
    try:
        DateManipulator(2023, 2, 29)
    except ValueError as e:
        print(f"Successfully caught error for non-leap year Feb 29th: {e}")