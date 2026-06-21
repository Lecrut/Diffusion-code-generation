from datetime import datetime

def get_year_delta(first: datetime, second: datetime) -> int:
    total_years = second.year - first.year
    first_moment = first.replace(year=second.year)
    if second < first_moment:
        total_years -= 1
    return total_years

if __name__ == '__main__':
    d1 = datetime(1985, 11, 12)
    d2 = datetime(2023, 11, 11)
    delta = get_year_delta(d1, d2)
    print(delta)