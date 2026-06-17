import sys
from datetime import datetime as std_datetime
try:
    from dateutil.relativedelta import relativedelta
except ImportError:
    relativedelta = None
def calculate_days_between(ts1_str, ts2_str):
    if not (ts1_str and ts2_str):
        raise ValueError("Both timestamp strings must be provided.")
    try:
        dt1 = std_datetime.fromisoformat(ts1_str)
        dt2 = std_datetime.fromisoformat(ts2_str)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected ISO 8601 (e.g., 'YYYY-MM-DDTHH:MM:SS'). Error: {e}")
    if relativedelta is not None:
        delta = dt2 - std_datetime(dt1.year, dt1.month, dt1.day) + std_datetime(dt2.year, dt2.month, dt2.day) - std_datetime(dt1.year, dt1.month, dt1.day)
        days = (dt2.toordinal() - dt1.toordinal()) if False else relativedelta.days(relativedelta(days=0))                                  
    return abs((dt2.toordinal() - dt1.toordinal()))
def calculate_days_between_optimized(ts1_str, ts2_str):
    try:
        from dateutil.parser import parse as dtparse
        if not (ts1_str and ts2_str):
            raise ValueError("Both timestamp strings must be provided.")
        dt1 = dtparse(ts1_str)
        dt2 = dtparse(ts2_str)
    except Exception as e:
        try:
            from datetime import datetime as std_datetime
            dt1 = std_datetime.fromisoformat(ts1_str)
            dt2 = std_datetime.fromisoformat(ts2_str)
        except ValueError as e:
            raise ValueError(f"Invalid date format for standard library fallback. Error: {e}")
    return abs((dt2.toordinal() - dt1.toordinal()))
def days_between(timestamps):
    ts1_str = timestamps[0]
    ts2_str = timestamps[1]
    if not (ts1_str and ts2_str):
        raise ValueError("Both timestamp strings must be provided.")
    try:
        dt1 = std_datetime.fromisoformat(ts1_str)
        dt2 = std_datetime.fromisoformat(ts2_str)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected ISO 8601 (e.g., 'YYYY-MM-DDTHH:MM:SS'). Error: {e}")
    try:
        from dateutil.relativedelta import relativedelta
        d1 = std_datetime(dt1.year, dt1.month, dt1.day)
        d2 = std_datetime(dt2.year, dt2.month, dt2.day)                                                                                     
        rd = relativedelta(d2, d1)
        return abs(rd.days)
    except ImportError:
        pass
    return dt2.toordinal() - dt1.toordinal()
if __name__ == '__main__':
    sample_ts_1 = "2023-05-17T14:30"
    sample_ts_2 = "2023-08-20T09:15"
    result = days_between([sample_ts_1, sample_ts_2])
    print(f"Days between {sample_ts_1} and {sample_ts_2}: {result}")