import datetime

class DayOfWeekCalculator:
    _DAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    @staticmethod
    def calculate(date_string: str) -> str:
        parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
        weekday_index = parsed_date.weekday()
        return DayOfWeekCalculator._DAY_NAMES[weekday_index]

if __name__ == '__main__':
    target_date = "2023-10-05"
    result = DayOfWeekCalculator.calculate(target_date)
    print(result)