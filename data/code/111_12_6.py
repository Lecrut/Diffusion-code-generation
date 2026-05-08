class DateManipulator:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
        self._validate()
    def _validate(self):
        if not isinstance(self._year, int) or not isinstance(self._month, int) or not isinstance(self._day, int):
            raise TypeError("Year, month, and day must be integers.")
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
    print("--- Testing DateManipulator ---")
    try:
        date1 = DateManipulator(2023, 10, 25)
        print(f"Initial Date 1: {date1}")
        print(f"Extracted Date 1: {date1.get_date()}")
    except Exception as e:
        print(f"Error in Test Case 1: {e}")
    print("-" * 20)
    try:
        date2 = DateManipulator(2024, 2, 29)
        print(f"Initial Date 2 (Leap Day): {date2}")
        print(f"Extracted Date 2: {date2.get_date()}")
    except Exception as e:
        print(f"Error in Test Case 2: {e}")
    print("-" * 20)
    try:
        date3 = DateManipulator(2023, 2, 30)
        print(f"Initial Date 3 (Invalid Day): {date3}")
    except ValueError as e:
        print(f"Caught expected error for Test Case 3: {e}")
    print("-" * 20)
    try:
        date4 = DateManipulator(2023, 1, 1)
        print(f"Initial Date 4: {date4}")
        date4.set_year(2025)
        print(f"After setting year to 2025: {date4}")
        print(f"Extracted Date 4: {date4.get_date()}")
        date4.set_day(31)
        print(f"After setting day to 31: {date4}")
        print(f"Extracted Date 4: {date4.get_date()}")
    except Exception as e:
        print(f"Error in Test Case 4: {e}")
    print("-" * 20)
    try:
        date5 = DateManipulator(2023, 13, 15)
    except ValueError as e:
        print(f"Caught expected error for Test Case 5 (Invalid Month): {e}")