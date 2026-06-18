import datetime
from threading import Lock
class DateUtility:
    def add_months(self, date_obj: datetime.date, months: int) -> datetime.date:
        year = date_obj.year + (months // 12)
        month = date_obj.month + (months % 12) - 1
        days_in_month = self._get_days_in_year(year, month + 1)
        if date_obj.day > days_in_month:
            day = days_in_month
        else:
            day = date_obj.day
        return datetime.date(year, month + 1, day)
    def _get_days_in_year(self, year: int, month: int) -> int:
        months_with_30_days = [4, 6, 9, 11]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            is_leap_year = True
        else:
            is_leap_year = False
        if month in months_with_30_days:
            return 30
        elif month == 2:
            return 29 if is_leap_year else 28
        else:
            return 31
_date_lock = Lock()
def add_months_safe(date_obj: datetime.date, months: int) -> datetime.date:
    with _date_lock:
        utility_instance = DateUtility()
        return utility_instance.add_months(date_obj, months)
if __name__ == '__main__':
    today = datetime.date.today()
    result_date = add_months_safe(today, 6)
    print(result_date)