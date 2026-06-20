import datetime

class DayOfWeekCalculator:
    def get_day_of_week(self, date_str):
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date.strftime('%A').upper()

if __name__ == '__main__':
    calculator = DayOfWeekCalculator()
    day_of_week = calculator.get_day_of_week('2023-11-11')
    print(day_of_week)