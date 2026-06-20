import datetime

class DayOfWeekCalculator:
    def get_day_of_week(self, date_str):
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        day_of_week = date_obj.strftime('%A').upper()
        return day_of_week

if __name__ == '__main__':
    calculator = DayOfWeekCalculator()
    sample_date = '2023-11-11'
    result = calculator.get_day_of_week(sample_date)
    print(result)