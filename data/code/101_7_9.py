import datetime

class DateWeekdayCalculator:
    def get_weekday_name(self, year, month, day):
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime('%A')

if __name__ == '__main__':
    calculator = DateWeekdayCalculator()
    weekday_name = calculator.get_weekday_name(2024, 7, 4)
    print(weekday_name)