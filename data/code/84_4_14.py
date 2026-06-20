from datetime import datetime

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_day_of_year(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None

class DayOfYearCalculator:
    def calculate_day_of_year(self, date_string):
        return get_day_of_year(date_string)

if __name__ == '__main__':
    calculator = DayOfYearCalculator()
    test_dates = [
        '2023-10-27',
        '2024-01-01',
        '1999-12-31',
        '2023-02-29',
        'invalid-date'
    ]
    for date_str in test_dates:
        day_num = calculator.calculate_day_of_year(date_str)
        print(f"Date: {date_str}, Day of Year: {day_num}")