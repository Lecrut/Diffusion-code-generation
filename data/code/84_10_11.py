class DateCalculator:
    def get_day_of_year(self, year, month, day):
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            months[2] = 29
        return sum(months[:month]) + day

if __name__ == '__main__':
    calculator = DateCalculator()
    print(calculator.get_day_of_year(2023, 10, 5))