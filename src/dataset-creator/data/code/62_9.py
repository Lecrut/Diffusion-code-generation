import datetime
from threading import Lock
class DateUtility:
    def add_months(self, date_obj: datetime.date, months: int) -> datetime.date:
        lock = self._lock
        with lock:
            year = date_obj.year + (months // 12)
            month = date_obj.month + (months % 12)
            while month > 13:
                month -= 12
                year += 1
            try:
                return datetime.date(year, month, date_obj.day)
            except ValueError:
                last_day_of_month = datetime.date(year, month, 0).day
                if months < 0 and date_obj.day > last_day_of_month:
                    prev_month_last_day = datetime.date(year, month - 1, 0).day
                    return datetime.date(year, month + (months % 12), max(1, min(date_obj.day, prev_month_last_day)))
                else:
                    return datetime.date(year, month, last_day_of_month)
    def __init__(self):
        self._lock = Lock()
if __name__ == '__main__':
    utility = DateUtility()
    today = datetime.date.today()
    result = utility.add_months(today, 3)
    print(result.strftime('%Y-%m-%d'))