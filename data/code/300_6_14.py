import datetime

class DateUtils:
    @staticmethod
    def days_remaining(year, month):
        today = datetime.date.today()
        last_day_of_month = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
        return (last_day_of_month - today).days

if __name__ == '__main__':
    year1 = 2024
    month1 = 3
    print(f"Days remaining in {year1}-{month1}: {DateUtils.days_remaining(year1, month1)}")
    year2 = 2023
    month2 = 2
    print(f"Days remaining in {year2}-{month2}: {DateUtils.days_remaining(year2, month2)}")
    year3 = 2024
    month3 = 12
    print(f"Days remaining in {year3}-{month3}: {DateUtils.days_remaining(year3, month3)}")