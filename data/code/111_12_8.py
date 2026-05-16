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
        print("\nTest 1: Valid Date Creation (2023-10-27)")
        date1 = DateManipulator(2023, 10, 27)
        print(f"Original: {date1}")
        print(f"Extracted: Year={date1.get_date()[0]}, Month={date1.get_date()[1]}, Day={date1.get_date()[2]}")
        print("\nTest 3: Setting Month (Valid)")
        date1.set_month(12)
        print(f"New Date: {date1}")
        print("\nTest 4: Setting Month (Invalid)")
        try:
            date1.set_month(13)
        except ValueError as e:
            print(f"Caught expected error: {e}")
        print(f"Date remains: {date1}")
        print("\nTest 5: Setting Day (Valid - 31st)")
        date1.set_day(31)
        print(f"New Date: {date1}")
        print("\nTest 6: Setting Day (Invalid - 32nd)")
        try:
            date1.set_day(32)
        except ValueError as e:
            print(f"Caught expected error: {e}")
        print(f"Date remains: {date1}")
        print("\nTest 7: Leap Year Validation (2024 is a leap year)")
        date2 = DateManipulator(2024, 2, 29)
        print(f"Valid Leap Date: {date2}")
        print("\nTest 8: Leap Year Validation (2023 is not a leap year)")
        try:
            date2.set_day(29)
        except ValueError as e:
            print(f"Caught expected error: {e}")
        print(f"Date remains: {date2}")
        print("\nTest 9: Setting Year")
        date2.set_year(2025)
        print(f"New Date: {date2}")
    except Exception as e:
        print(f"\nAn unexpected error occurred during testing: {e}")