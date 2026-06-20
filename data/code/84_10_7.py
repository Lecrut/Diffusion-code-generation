class DateCalculator:
    def get_day_of_year(self, year, month, day):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[1] = 29
        return sum(days_in_month[:month - 1]) + day

if __name__ == '__main__':
    calculator = DateCalculator()
    day_number = calculator.get_day_of_year(2023, 10, 27)
    print(day_number)