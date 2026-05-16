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
            raise ValueError("Invalid day after addition")
    def add_months(self, months):
        new_month = self._month + months
        new_year = self._year + (new_month - 12) // 12
        new_month = (new_month - 1) % 12 + 1
        self._year = new_year
        self._month = new_month
        self._day = self._day
if __name__ == '__main__':
    initial_year = 2023
    initial_month = 10
    initial_day = 25
    date1 = DateManipulator(initial_year, initial_month, initial_day)
    print(f"Original Date: Year={date1.get_year()}, Month={date1.get_month()}, Day={date1.get_day()}")
    print("-" * 20)
    date2 = DateManipulator(2024, 1, 15)
    print(f"Original Date: Year={date2.get_year()}, Month={date2.get_month()}, Day={date2.get_day()}")
    date2.add_days(10)
    print(f"After adding 10 days: Year={date2.get_year()}, Month={date2.get_month()}, Day={date2.get_day()}")
    print("-" * 20)
    date3 = DateManipulator(2023, 12, 31)
    print(f"Original Date: Year={date3.get_year()}, Month={date3.get_month()}, Day={date3.get_day()}")
    date3.add_months(1)
    print(f"After adding 1 month: Year={date3.get_year()}, Month={date3.get_month()}, Day={date3.get_day()}")
    date4 = DateManipulator(2023, 1, 1)
    print(f"Original Date: Year={date4.get_year()}, Month={date4.get_month()}, Day={date4.get_day()}")
    try:
        date4.add_days(-5)
        print(f"After subtracting 5 days: Year={date4.get_year()}, Month={date4.get_month()}, Day={date4.get_day()}")
    except ValueError as e:
        print(f"Error: {e}")