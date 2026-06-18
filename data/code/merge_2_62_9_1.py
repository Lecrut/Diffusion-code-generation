import datetime
from threading import Lock
class DateUtility:
    def add_months(self, date_obj: datetime.date, months: int) -> datetime.date:
        year = date_obj.year + (months // 12)
        month = date_obj.month + (months % 12)
        while True:
            try:
                new_date = datetime.date(year, month, date_obj.day)
                break
            except ValueError:
                day = min(date_obj.day - 1, 30 if len(str(month)) == 1 else 28 or (datetime.datetime(year, month + 1, 1).day - 1))
                new_date = datetime.date(year, month, day)
        return new_date
def add_months_thread_safe(date_obj: datetime.date, months: int) -> datetime.date:
    lock = Lock()
    with lock:
        year = date_obj.year + (months // 12)
        month = date_obj.month + (months % 12)
        while True:
            try:
                new_date = datetime.date(year, month, date_obj.day)
                break
            except ValueError:
                day = min(date_obj.day - 1, 30 if len(str(month)) == 1 else 28 or (datetime.datetime(year, month + 1, 1).day - 1))
                new_date = datetime.date(year, month, day)
        return new_date
if __name__ == '__main__':
    today = datetime.date.today()
    result = add_months_thread_safe(today, 6)
    print(result)