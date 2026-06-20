import datetime

class DateCalculator:
    def get_day_of_year(self, year, month, day):
        date = datetime.date(year, month, day)
        return date.timetuple().tm_yday

if __name__ == '__main__':
    calculator = DateCalculator()
    year1 = 2023
    month1 = 10
    day1 = 27
    result1 = calculator.get_day_of_year(year1, month1, day1)
    print(f"Day of the year for {year1}-{month1:02d}-{day1:02d} is: {result1}")