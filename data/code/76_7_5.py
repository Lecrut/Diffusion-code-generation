from datetime import date, timedelta

class DateUtils:
    @staticmethod
    def days_until_new_year(year):
        today = date.today()
        new_year = date(year + 1, 1, 1)
        return (new_year - today).days

if __name__ == '__main__':
    sample_year = 2024
    print(DateUtils.days_until_new_year(sample_year))