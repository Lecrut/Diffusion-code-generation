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
            if new_day > 31:
                new_day = 31
            if new_day == 31:
                new_month += 1
                new_day = 1
        elif new_day < 1:
            new_month -= 1
            new_day += (31 - abs(new_day - 1))
            if new_month == 0:
                new_year -= 1
                new_month = 1
                new_day = 31
        self._year = new_year
        self._month = new_month
        self._day = new_day
if __name__ == '__main__':
    original_year = 2023
    original_month = 10
    original_day = 25
    date1 = DateManipulator(original_year, original_month, original_day)
    print(f"Original Date: Year={date1.get_year()}, Month={date1.get_month()}, Day={date1.get_day()}")
    print("-" * 20)
    date2 = DateManipulator(original_year, original_month, original_day)
    date2.add_days(10)
    print(f"Date after adding 10 days: Year={date2.get_year()}, Month={date2.get_month()}, Day={date2.get_day()}")
    print("-" * 20)
    date3 = DateManipulator(2023, 12, 31)
    date3.add_days(1)
    print(f"Date after adding 1 day to Dec 31st: Year={date3.get_year()}, Month={date3.get_month()}, Day={date3.get_day()}")
    date4 = DateManipulator(2023, 1, 1)
    date4.add_days(-5)
    print(f"Date after subtracting 5 days from Jan 1st: Year={date4.get_year()}, Month={date4.get_month()}, Day={date4.get_day()}")