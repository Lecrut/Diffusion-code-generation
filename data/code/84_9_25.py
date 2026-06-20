class DateCalculator:
    def __init__(self):
        self.days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self, year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def calculate_day_of_year(self, date_obj):
        if self.is_leap_year(date_obj.year):
            self.days_in_month[2] = 29
        else:
            self.days_in_month[2] = 28
        day_of_year = sum(self.days_in_month[:date_obj.month]) + date_obj.day
        return day_of_year

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date1 = (2023, 4, 15)
    result1 = calculator.calculate_day_of_year(date(sample_date1[0], sample_date1[1], sample_date1[2]))
    print(f"Date: {sample_date1} -> Day of Year: {result1}")
    sample_date2 = (2020, 2, 29)
    result2 = calculator.calculate_day_of_year(date(sample_date2[0], sample_date2[1], sample_date2[2]))
    print(f"Date: {sample_date2} -> Day of Year: {result2}")