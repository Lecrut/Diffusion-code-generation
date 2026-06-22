from datetime import date, timedelta

class DateCalculator:
    ADD_DAYS = 30
    BASE_YEAR = 2024
    BASE_MONTH = 7
    BASE_DAY = 4

    @staticmethod
    def get_base_date():
        return date(DateCalculator.BASE_YEAR, DateCalculator.BASE_MONTH, DateCalculator.BASE_DAY)

    @staticmethod
    def add_days(target_date, days):
        return target_date + timedelta(days=days)

    @staticmethod
    def format_date(d):
        return d.strftime("%Y-%m-%d")

def calculate_future_date():
    base = DateCalculator.get_base_date()
    future = DateCalculator.add_days(base, DateCalculator.ADD_DAYS)
    return DateCalculator.format_date(future)

if __name__ == '__main__':
    print(calculate_future_date())