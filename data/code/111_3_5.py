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
        new_year = self._year
        new_month = self._month
        new_day = self._day + days
        if new_day > 31:
            new_month += (new_day - 31) // 30
            new_day = new_day % 30
            if new_day == 0:
                new_day = 30
            if new_day > 30:
                new_day = 30
            if new_day == 31:
                new_day = 31
            if new_day > 31:
                new_month += 1
                new_day = new_day - 31
                if new_day == 0:
                    new_day = 30
        if new_month > 12:
            new_year += (new_month - 1) // 12
            new_month = (new_month - 1) % 12 + 1
        self._year = new_year
        self._month = new_month
        self._day = new_day
if __name__ == '__main__':
    original_year = 2023
    original_month = 10
    original_day = 25
    date1 = DateManipulator(original_year, original_month, original_day)
    print(f"Original Date: Year={date1.get_year()}, Month={date1.get_month()}, Day={date1.get_day()}")
    date1.add_days(10)
    print(f"After adding 10 days: Year={date1.get_year()}, Month={date1.get_month()}, Day={date1.get_day()}")
    date2 = DateManipulator(2024, 1, 31)
    print(f"Original Date 2: Year={date2.get_year()}, Month={date2.get_month()}, Day={date2.get_day()}")
    date2.add_days(1)
    print(f"After adding 1 day: Year={date2.get_year()}, Month={date2.get_month()}, Day={date2.get_day()}")