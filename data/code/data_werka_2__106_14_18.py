from datetime import datetime

def diff_years(dt_a: datetime, dt_b: datetime) -> int:
    if dt_a.year == dt_b.year:
        return 0
    if dt_a.year > dt_b.year:
        return dt_a.year - dt_b.year
    return dt_b.year - dt_a.year

if __name__ == '__main__':
    t1 = datetime(2023, 10, 15)
    t2 = datetime(2019, 5, 20)
    print(diff_years(t1, t2))