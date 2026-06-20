import calendar

class DateDifferenceCalculator:
    def __init__(self):
        self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def month_index(self, month_name):
        return self.months.index(month_name)

    def months_between_dates(self, date_str1, date_str2):
        year1, month1, day1 = map(int, date_str1.split('-'))
        year2, month2, day2 = map(int, date_str2.split('-'))
        start_month_index = self.month_index(calendar.month_name[month1])
        end_month_index = self.month_index(calendar.month_name[month2])
        difference = (year2 - year1) * 12 + (end_month_index - start_month_index)
        return difference

if __name__ == '__main__':
    calculator = DateDifferenceCalculator()
    date_str1 = '2020-01-01'
    date_str2 = '2023-04-15'
    result = calculator.months_between_dates(date_str1, date_str2)
    print(result)