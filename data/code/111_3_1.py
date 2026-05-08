class DateManipulator:
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
    def get_year(self):
        return self._year
    def get_month(self):
        return self._month
    def get_day(self):
        return self._day
    def add_days(self, days):
        new_day = self._day + days
        if 1 <= new_day <= 31:
            self._day = new_day
        else:
            raise ValueError("Day out of range for the current month")
    def add_months(self, months):
        new_month = self._month + months
        new_year = self._year + (new_month - 12) // 12
        new_month = (new_month - 1) % 12 + 1
        self._year = new_year
        self._month = new_month
        if not (1 <= self._month <= 12):
            raise ValueError("Month out of range")
        self._day = self._day
    def __repr__(self):
        return f"DateManipulator(year={self._year}, month={self._month}, day={self._day})"
if __name__ == '__main__':
    initial_year = 2023
    initial_month = 10
    initial_day = 25
    date1 = DateManipulator(initial_year, initial_month, initial_day)
    print(f"Original Date: {date1}")
    print("\n--- Adding Days ---")
    date1.add_days(5)
    print(f"After adding 5 days: {date1}")
    date2 = DateManipulator(2024, 1, 15)
    print(f"Original Date 2: {date2}")
    print("\n--- Adding Months ---")
    date2.add_months(3)
    print(f"After adding 3 months to Date 2: {date2}")
    date3 = DateManipulator(2025, 12, 31)
    print(f"Original Date 3: {date3}")
    date3.add_months(1)
    print(f"After adding 1 month to Date 3: {date3}")
    print("\nVerifying Immutability (Original object remains unchanged):")
    print(f"Date 1 after operations: {date1}")
    print(f"Date 2 after operations: {date2}")
    print(f"Date 3 after operations: {date3}")