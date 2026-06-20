import datetime

class DateCalculator:
    def get_day_of_week(self, date_object):
        return date_object.weekday()

if __name__ == '__main__':
    calculator = DateCalculator()
    sample_date = datetime.date(2024, 7, 4)
    day_of_week = calculator.get_day_of_week(sample_date)
    print(day_of_week)