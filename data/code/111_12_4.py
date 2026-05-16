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
        pass
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
        if not (1 <= new_month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        self._month = new_month
        self._validate()
    def set_day(self, new_day):
        if not isinstance(new_day, int):
            raise TypeError("Day must be an integer.")
        year = self._year
        month = self._month
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]
        if month == 2 and is_leap:
            days_in_month = 29
        if not (1 <= new_day <= days_in_month):
            raise ValueError(f"Day {new_day} is invalid for month {self._month} in year {self._year}.")
        self._day = new_day
        self._validate()
    def __str__(self):
        return f"{self._year}-{self._month:02d}-{self._day:02d}"
if __name__ == '__main__':
    print("--- Test Case 1: Valid Initial Date ---")
    try:
        date1 = DateManipulator(2023, 10, 25)
        print(f"Initial Date: {date1}")
        print(f"Extracted: {date1.get_date()}")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 2: Setting and Modifying ---")
    try:
        date2 = DateManipulator(2024, 2, 29)                 
        print(f"Initial Date: {date2}")
        date2.set_month(3)
        print(f"After setting month to 3: {date2}")
        date2.set_day(31)
        print(f"After setting day to 31: {date2}")
        print("\nAttempting invalid day setting:")
        date2.set_day(30)                        
    except ValueError as ve:
        print(f"Caught expected error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("\n--- Test Case 3: Invalid Month/Day Creation ---")
    try:
        DateManipulator(2023, 13, 1)
    except ValueError as ve:
        print(f"Caught expected error for invalid month: {ve}")
    print("\n--- Test Case 4: Leap Year Validation (Setting to valid leap day) ---")
    try:
        date3 = DateManipulator(2024, 2, 29)
        print(f"Valid Leap Date: {date3}")
    except Exception as e:
        print(f"Error: {e}")
    print("\n--- Test Case 5: Setting to invalid day in non-leap year ---")
    try:
        date4 = DateManipulator(2023, 2, 29)
        print(f"Attempting to set Feb 29th in 2023:")
        date4.set_day(29)
    except ValueError as ve:
        print(f"Caught expected error for non-leap year: {ve}")