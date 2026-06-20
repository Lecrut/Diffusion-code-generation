from datetime import date

class DateCalculator:
    def __init__(self, year, month, day):
        self.date_obj = date(year, month, day)

    def get_day_of_year(self):
        return self.date_obj.timetuple().tm_yday

if __name__ == '__main__':
    calc1 = DateCalculator(2024, 3, 15)
    calc2 = DateCalculator(2000, 1, 1)
    calc3 = DateCalculator(2023, 12, 31)
    print(f"Day of year for {calc1.date_obj}: {calc1.get_day_of_year()}")
    print(f"Day of year for {calc2.date_obj}: {calc2.get_day_of_year()}")
    print(f"Day of year for {calc3.date_obj}: {calc3.get_day_of_year()}")