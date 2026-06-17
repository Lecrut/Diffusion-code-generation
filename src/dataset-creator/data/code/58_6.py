import datetime
from dateutil.relativedelta import relativedelta as rd                          
try:
    from dateutil.parser import parse as d_parse
except ImportError:
    def d_parse(s):
        return datetime.datetime.strptime(str(s), "%Y-%m-%d") if isinstance(s, str) else s
def days_between(ts1_str, ts2_str):
    try:
        t1 = rd.parse(ts1_str).replace(hour=0, minute=0, second=0, microsecond=0)
        t2 = rd.parse(ts2_str).replace(hour=0, minute=0, second=0, microsecond=0)
    except Exception:
        try:
            if isinstance(ts1_str, str):
                t1 = datetime.datetime.strptime(str(ts1_str), "%Y-%m-%d")
            else:
                raise ValueError("Invalid input format for ts1")
            if isinstance(ts2_str, str):
                t2 = datetime.datetime.strptime(str(ts2_str), "%Y-%m-%d")
            else:
                raise ValueError("Invalid input format for ts2")
        except Exception as e:
            raise ValueError(f"Date parsing failed: {e}")
    if not isinstance(t1, datetime.datetime) or not isinstance(t2, datetime.datetime):
        raise TypeError("Inputs must be parseable to datetime objects.")
    delta = t2 - t1
    return int(delta.total_seconds() // 86400)
if __name__ == '__main__':
    result = days_between("2023-01-01", "2023-12-31")
    print(result)