from datetime import timedelta

class DateUtils:
    @staticmethod
    def days_until_new_year(year):
        from datetime import date
        today = date.today()
        new_year = date(year, 12, 31)
        return (new_year - today).days + 1 if today <= new_year else None

if __name__ == '__main__':
    print(DateUtils.days_until_new_year(2024))