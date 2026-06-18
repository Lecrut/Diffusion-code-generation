import datetime
from dateutil.relativedelta import relativedelta as rd                          
try:
    from dateutil.parser import parse as d_parse
except ImportError:
    def d_parse(s):
        return datetime.datetime.strptime(str(s), "%Y-%m-%d")
def days_between(ts1, ts2):
    if not isinstance(ts1, (str, datetime.date, datetime.datetime)) or\
       not isinstance(ts2, (str, datetime.date, datetime.datetime)):
        raise ValueError("Inputs must be strings representing dates or date/datetime objects.")
    try:
        d1 = d_parse(str(ts1)) if isinstance(ts1, str) else ts1.replace(hour=0, minute=0, second=0, microsecond=0)
        d2 = d_parse(str(ts2)) if isinstance(ts2, str) else ts2.replace(hour=0, minute=0, second=0, microsecond=0)
    except Exception:
        raise ValueError("Invalid date format provided.")
    try:
        return int(rd(d1).days - rd(d2).days)
    except AttributeError:
        delta = d2 - d1
        if delta.days < 0:
            return -(abs(delta.days))
        else:
            return abs(delta.days)
if __name__ == '__main__':
    print(days_between("2023-01-01", "2024-06-15"))