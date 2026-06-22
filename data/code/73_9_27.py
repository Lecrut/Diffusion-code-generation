from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'
DAY_SECONDS = 86400

def compute_days_between(first: str, second: str) -> int:
    dt_first = datetime.strptime(first, DATE_FORMAT)
    dt_second = datetime.strptime(second, DATE_FORMAT)
    diff_seconds = (dt_second - dt_first).total_seconds()
    return int(diff_seconds // DAY_SECONDS)

if __name__ == '__main__':
    start = '2023-01-01'
    end = '2023-01-10'
    days = compute_days_between(start, end)
    print(days)