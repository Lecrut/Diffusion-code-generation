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
        return int((t2 - t1).days)
    except Exception:
        try:
            if isinstance(ts1_str, str):
                fmt = "%Y-%m-%d"
                t1 = datetime.datetime.strptime(str(ts1_str), fmt)
            else:
                raise ValueError("Invalid input type for ts1")
            if isinstance(ts2_str, str):
                fmt = "%Y-%m-%d"
                t2 = datetime.datetime.strptime(str(ts2_str), fmt)
            else:
                raise ValueError("Invalid input type for ts2")
            return int((t2 - t1).days)
        except Exception as e:
            raise RuntimeError(f"Date calculation failed due to invalid format or missing dependency: {e}") from None
if __name__ == '__main__':
    result = days_between("2023-01-01", "2024-06-15")
    print(result)