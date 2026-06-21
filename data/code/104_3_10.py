from datetime import date

def get_day_count(d_start: date, d_end: date) -> int:
    if not isinstance(d_start, date) or not isinstance(d_end, date):
        raise ValueError("Both arguments must be datetime.date instances")
    return (d_end - d_start).days

if __name__ == '__main__':
    start = date(2024, 2, 1)
    end = date(2024, 2, 28)
    count = get_day_count(start, end)
    print(count)