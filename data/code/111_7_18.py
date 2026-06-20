class Date:
    MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    LEAP_FEBRUARY = 29

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def add_days(self, days):
        while days > 0:
            if self.day == Date.MONTHS[self.month] + int(Date.is_leap_year(self.year) and self.month == 2):
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
            else:
                self.day += 1
                days -= 1

    def add_years(self, years):
        self.year += years

def main():
    date = Date(2020, 12, 31)
    date.add_years(1)
    date.add_days(1)
    print(f"Resulting date: {date.day}/{date.month}/{date.year}")

if __name__ == '__main__':
    main()