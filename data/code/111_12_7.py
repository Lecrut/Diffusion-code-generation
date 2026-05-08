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
        try:
            import calendar
            max_days = calendar.monthrange(self._year, self._month)[1]
            if self._day > max_days:
                raise ValueError("Day is invalid for the given month and year.")
        except ImportError:
            pass 
        except ValueError as e:
            raise ValueError(f"Date validation failed: {e}")
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
        date1.set_year(2024)
        date1.set_day(31)
        print(f"Modified Date 1: {date1}")
    except Exception as e:
        print(f"Error in Test Case 1: {e}")
    print("\n" + "="*30 + "\n")
    try:
        date2 = DateManipulator(2024, 2, 29)
        print(f"Initial Date 2 (Leap Year): {date2}")
        date2.set_year(2023)
        print(f"Attempting to set date to 2023-02-29...")
    except ValueError as e:
        print(f"Successfully caught expected error for invalid date: {e}")
    except Exception as e:
        print(f"Unexpected error in Test Case 2: {e}")
    print("\n" + "="*30 + "\n")
    try:
        date3 = DateManipulator(2025, 13, 15)
        print(f"Attempting to create date with invalid month (13): {date3}")
    except ValueError as e:
        print(f"Successfully caught expected error for invalid month: {e}")
    except Exception as e:
        print(f"Unexpected error in Test Case 3: {e}")
    print("\n" + "="*30 + "\n")
    try:
        date4 = DateManipulator(2023, 4, 31)
        print(f"Attempting to create date with invalid day (April 31st): {date4}")
    except ValueError as e:
        print(f"Successfully caught expected error for invalid day: {e}")
    except Exception as e:
        print(f"Unexpected error in Test Case 4: {e}")