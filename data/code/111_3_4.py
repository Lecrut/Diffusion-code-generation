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
            if new_day == 31 and new_month > 12:
                new_month += 1
                new_day = 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        if new_month > 12:
            new_month = 1
            new_year += 1
        if new_month > 12:
            new_month = 1
            new_year += 1
        self._year = new_year
        self._month = new_month
        self._day = new_day
    def add_months(self, months):
        new_year = self._year + (self._month + months - 1) // 12
        new_month = (self._month + months - 1) % 12 + 1
        self._year = new_year
        self._month = new_month
        self._day = self._day
if __name__ == '__main__':
    original_year = 2023
    original_month = 10
    original_day = 25
    date1 = DateManipulator(original_year, original_month, original_day)
    print(f"Original Date: {date1.get_year()}-{date1.get_month()}-{date1.get_day()}")
    print("-" * 20)
    date2 = DateManipulator(original_year, original_month, original_day)
    date2.add_days(10)
    print(f"Date after adding 10 days: {date2.get_year()}-{date2.get_month()}-{date2.get_day()}")
    print("-" * 20)
    date3 = DateManipulator(2023, 12, 31)
    date3.add_days(1)
    print(f"Date after adding 1 day to Dec 31: {date3.get_year()}-{date3.get_month()}-{date3.get_day()}")
    print("-" * 20)
    date4 = DateManipulator(2023, 1, 30)
    date4.add_months(2)
    print(f"Date after adding 2 months to Jan 30: {date4.get_year()}-{date4.get_month()}-{date4.get_day()}")
    print("-" * 20)
    date5 = DateManipulator(2023, 1, 30)
    date5.add_months(13)
    print(f"Date after adding 13 months to Jan 30: {date5.get_year()}-{date5.get_month()}-{date5.get_day()}")