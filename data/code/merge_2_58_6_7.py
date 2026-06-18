import datetime
from dateutil.relativedelta import relativedelta as drd                                
def calculate_days_between(ts1_str: str, ts2_str: str) -> int:
    try:
        dt1 = datetime.datetime.fromisoformat(ts1_str.replace('Z', '+00:00')) if 'T' in ts1_str else datetime.datetime.strptime(ts1_str, '%Y-%m-%d')
        dt2 = datetime.datetime.fromisoformat(ts2_str.replace('Z', '+00:00')) if 'T' in ts2_str else datetime.datetime.strptime(ts2_str, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected ISO or YYYY-MM-DD. Error: {e}")
    try:
        delta = drd(days=0).between(dt1, dt2)
        return abs(delta.days) if hasattr(delta, 'days') else int(abs((dt2 - dt1).total_seconds() / 86400))
    except Exception as e:
        fallback_delta = datetime.timedelta(days=int(abs((dt2 - dt1).total_seconds() / 86400)))
        return abs(fallback_delta.days)
if __name__ == '__main__':
    result = calculate_days_between("2023-01-01", "2023-12-31")
    print(result)