import calendar

class DateCalculator:
    def __init__(self):
        self.months = [month for month in calendar.month_name[1:]]

    def get_month_index(self, month_str):
        return self.months.index(month_str)

    def months_between_dates(self, date_str1, date_str2):
        year1, month1, day1 = map(int, date_str1.split('-'))
        year2, month2, day2 = map(int, date_str2.split('-'))
        start_month_index = self.get_month_index(calendar.month_name[month1])
        end_month_index = self.get_month_index(calendar.month_name[month2])
        difference = (year2 - year1) * 12 + (end_month_index - start_month_index)
        return abs(difference)

if __name__ == '__main__':
    calculator = DateCalculator()
    date_str1 = '2020-03-15'
    date_str2 = '2024-07-20'
    result = calculator.months_between_dates(date_str1, date_str2)
    print(result)