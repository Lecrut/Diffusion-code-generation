import datetime

class DateOfWeekCalculator:
    def calculate_weekday(self, year, month, day):
        date_obj = datetime.date(year, month, day)
        return date_obj.weekday()

if __name__ == '__main__':
    calculator = DateOfWeekCalculator()
    sample_date = (2024, 7, 4)
    weekday_number = calculator.calculate_weekday(*sample_date)
    print(weekday_number)