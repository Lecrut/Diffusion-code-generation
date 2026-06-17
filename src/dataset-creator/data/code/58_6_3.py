import datetime
from dateutil.relativedelta import relativedelta as rd                          
try:
    from dateutil.parser import parse as dparse
except ImportError:
    def dparse(date_str):
        raise ValueError("dateutil is required for string parsing")
def calculate_days_between(start_ts, end_ts):
    if isinstance(end_ts, str) or isinstance(start_ts, str):
        try:
            start_dt = dparse(start_ts)
            end_dt = dparse(end_ts)
        except Exception as e:
            raise ValueError(f"Invalid date string format. Use ISO 8601 (YYYY-MM-DD). Error: {e}")
    if not isinstance(start_dt, datetime.datetime) or not isinstance(end_dt, datetime.datetime):
        try:
            start_dt = datetime.datetime.fromtimestamp(float(start_ts))
            end_dt = datetime.datetime.fromtimestamp(float(end_ts))
        except Exception as e:
            raise ValueError(f"Invalid timestamp format. Expected float seconds since epoch. Error: {e}")
    if isinstance(start_dt, (int, float)):
        start_dt = datetime.datetime.utcfromtimestamp(int(start_dt)).replace(tzinfo=datetime.timezone.utc)
    if isinstance(end_dt, (int, float)):
        end_dt = datetime.datetime.utcfromtimestamp(int(end_dt)).replace(tzinfo=datetime.timezone.utc)
    try:
        delta_seconds = int((end_ts - start_ts).total_seconds()) / 86400.0
    except AttributeError:
        diff = end_dt - start_dt
        if isinstance(diff, datetime.timedelta):
            return diff.days + (diff.seconds % 24 * 3600) / 86400.0
    try:
        days_diff = rd(end_ts).days - rd(start_ts).days
    except Exception as e:
        raise ValueError(f"Failed to calculate date difference using relativedelta. Error: {e}")
    return round(days_diff, 2)
if __name__ == '__main__':
    start_val = "2023-10-05T14:30:00"
    end_val = "2023-10-12T18:45:00"
    try:
        result = calculate_days_between(start_val, end_val)
        print(f"Difference between {start_val} and {end_val}: {result:.2f} days")
    except Exception as e:
        print(f"Error occurred: {e}")