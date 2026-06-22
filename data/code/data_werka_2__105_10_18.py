from datetime import datetime, timedelta

def get_next_day(date_str: str) -> datetime:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    next_dt = dt + timedelta(days=1)
    return next_dt

if __name__ == '__main__':
    result = get_next_day("2023-10-31")
    print(result)