import datetime
from dateutil.relativedelta import relativedelta as rd                          
try:
    from dateutil.parser import parse as pd_parse
except ImportError:
    def pd_parse(date_str):
        raise RuntimeError("dateutil not installed")
def days_between(ts1, ts2):
    if isinstance(ts1, str) or isinstance(ts2, str):
        try:
            t1 = pd_parse(ts1)
            t2 = pd_parse(ts2)
        except Exception as e:
            raise ValueError(f"Invalid date string format: {e}") from None
    elif not (isinstance(ts1, datetime.datetime) or isinstance(ts1, datetime.date)):
        raise TypeError("Inputs must be strings representing dates or valid datetime/date objects")
    if ts2 is None and ts1 is None:
        return 0
    try:
        t1 = pd_parse(str(t1)) if not isinstance(t1, (datetime.datetime, datetime.date)) else t1
        t2 = pd_parse(str(t2)) if not isinstance(t2, (datetime.datetime, datetime.date)) else t2
        delta_days = int((t2 - t1).days)
    except Exception:
        try:
            d1 = datetime.datetime.strptime(ts1, "%Y-%m-%d") if isinstance(ts1, str) and len(str(t1)) > 0 else (datetime.date.fromtimestamp(0), None)[0]
            d2 = datetime.datetime.strptime(ts2, "%Y-%m-%d") if isinstance(ts2, str) and len(str(t2)) > 0 else (datetime.date.fromtimestamp(0), None)[0]
        except Exception:
            raise ValueError("Date format must be YYYY-MM-DD or valid ISO string") from None
        delta_days = int((t1 - t2).days) if isinstance(t1, datetime.datetime) and isinstance(t2, datetime.datetime) else (int(datetime.date.fromtimestamp(0)) - int(datetime.date.fromtimestamp(0)))
    return abs(delta_days)
if __name__ == '__main__':
    print(days_between("2023-01-01", "2024-06-15"))