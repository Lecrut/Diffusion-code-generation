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
            if self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0):
                max_days = 29
            else:
                max_days = 28
        else:
            max_days = days_in_month[self._month]
        if self._day > max_days:
            raise ValueError(f"Day {self._day} is invalid for month {self._month} in year {self._year}.")
    def get_date(self):
        return (self._year, self._month, self._day)
    def set_year(self, new_year):
        if not isinstance(new_year, int):
            raise TypeError("Year must be an integer.")
        self._year = new_year
        self._validate()
    def set_month(self, new_month):
        if not isinstance(new_month, int):
            raise TypeError("Month must be an integer.")
        self._month = new_month
        self._validate()
    def set_day(self, new_day):
        if not isinstance(new_day, int):
            raise TypeError("Day must be an integer.")
        self._day = new_day
        self._validate()
    def __str__(self):
        return f"{self._year}-{self._month:02d}-{self._day:02d}"
if __name__ == '__main__':
    print("--- Test Case 1: Valid Date ---")
    try:
        date1 = DateManipulator(2023, 10, 25)
        print(f"Initial Date: {date1}")
        print(f"Extracted: {date1.get_date()}")
        date1.set_year(2024)
        print(f"After setting year to 2024: {date1}")
        date1.set_day(31)
        print(f"After setting day to 31: {date1}")
    except ValueError as e:
        print(f"Error during valid test: {e}")
    except TypeError as e:
        print(f"Error during valid test: {e}")
    print("\n--- Test Case 2: Leap Year Validation (February 29th) ---")
    try:
        date2 = DateManipulator(2024, 2, 29)
        print(f"Valid Leap Date: {date2}")
        date3 = DateManipulator(2023, 2, 29)
        print(f"Invalid Leap Date Attempt: {date3}")
    except ValueError as e:
        print(f"Caught expected error for invalid date: {e}")
    print("\n--- Test Case 3: Month Boundary Validation ---")
    try:
        date4 = DateManipulator(2023, 13, 15)
        print(f"Invalid Month Attempt: {date4}")
    except ValueError as e:
        print(f"Caught expected error for invalid month: {e}")
    print("\n--- Test Case 4: Day Boundary Validation (31 days in April) ---")
    try:
        date5 = DateManipulator(2023, 4, 31)
        print(f"Invalid Day Attempt: {date5}")
    except ValueError as e:
        print(f"Caught expected error for invalid day: {e}")
    print("\n--- Test Case 5: Setting to Invalid State (Year Change) ---")
    try:
        date6 = DateManipulator(2023, 2, 30)
        print(f"Initial State: {date6}")
        date6.set_year(2023)                                                                                                                   
        print(f"After setting year back: {date6}")
    except ValueError as e:
        print(f"Caught expected error during state change: {e}")