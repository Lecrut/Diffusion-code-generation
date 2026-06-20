class DateCalculator:
    def get_day_of_year(self, year, month, day):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29
        day_of_year = sum(days_in_month[:month]) + day
        return day_of_year

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_day_of_year(2023, 10, 27))
    print(calculator.get_day_of_year(2024, 2, 29))