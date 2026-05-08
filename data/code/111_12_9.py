class DateManipulator:
    def __init__(self, year, month, day):
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise TypeError("Year, month, and day must be integers.")
        self._year = year
        self._month = month
        self._day = day
        self._validate()
    def _validate(self):
        if not isinstance(self._year, int) or not isinstance(self._month, int) or not isinstance(self._day, int):
            raise ValueError("Invalid type for date components.")
        if not (1 <= self._month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= self._day <= 31):
            raise ValueError("Day must be between 1 and 31.")
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        is_leap = (self._year % 4 == 0 and self._year % 100 != 0) or (self._year % 400 == 0)
        max_days = days_in_month[self._month]
        if self._month == 2 and is_leap:
            max_days = 29
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
    print("--- Testing DateManipulator ---")
    try:
        date1 = DateManipulator(2023, 10, 25)
        print(f"Initial Date 1: {date1}")
        print(f"Year: {date1.get_year()}, Month: {date1.get_month()}, Day: {date1.get_day()}")
    except Exception as e:
        print(f"Error in Test Case 1: {e}")
    print("-" * 20)
    try:
        date2 = DateManipulator(2024, 2, 29)
        print(f"Initial Date 2 (Leap): {date2}")
        print(f"Year: {date2.get_year()}, Month: {date2.get_month()}, Day: {date2.get_day()}")
    except Exception as e:
        print(f"Error in Test Case 2: {e}")
    print("-" * 20)
    try:
        date3 = DateManipulator(2023, 2, 29)
        print(f"Date 3: {date3}")
    except ValueError as e:
        print(f"Successfully caught expected error for Test Case 3: {e}")
    except Exception as e:
        print(f"Unexpected error in Test Case 3: {e}")
    print("-" * 20)
    try:
        date4 = DateManipulator(2025, 1, 15)
        print(f"Initial Date 4: {date4}")
        date4.set_year(2026)
        print(f"After setting year to 2026: {date4}")
        date4.set_day(30)
        print(f"After setting day to 30: {date4}")
        print("\nAttempting to set invalid date (Feb 30th in 2024):")
        date4.set_month(2)
        date4.set_day(30)
    except ValueError as e:
        print(f"Successfully caught expected error during modification: {e}")
    except Exception as e:
        print(f"Error during Test Case 4 modification: {e}")
    print("-" * 20)
    try:
        date5 = DateManipulator(2024, 3, 1)
        print(f"Initial Date 5: {date5}")
        date5.set_year(2024)
        date5.set_month(3)
        date5.set_day(1)
        print(f"Final Date 5: {date5}")
    except Exception as e:
        print(f"Error in Test Case 5: {e}")