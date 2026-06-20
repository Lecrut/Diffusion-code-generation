import datetime

class DateCalculator:
    @staticmethod
    def get_day_of_week(date_str):
        date_object = datetime.date.fromisoformat(date_str)
        return date_object.weekday()

if __name__ == '__main__':
    calculator = DateCalculator()
    day_of_week = calculator.get_day_of_week('2024-07-04')
    print(day_of_week)