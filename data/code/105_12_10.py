from datetime import datetime, timedelta

class DateCalculator:

    def get_next_weekday(self, start_date_str, weekday):
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        target_day = start_date.weekday()
        days_to_add = (weekday - target_day) % 7
        if days_to_add == 0:
            days_to_add = 7
        next_weekday = start_date + timedelta(days=days_to_add)
        return next_weekday.strftime('%Y-%m-%d')
if __name__ == '__main__':
    calculator = DateCalculator()
    start_date = '2023-10-01'
    weekday = 4
    result = calculator.get_next_weekday(start_date, weekday)
    print(result)