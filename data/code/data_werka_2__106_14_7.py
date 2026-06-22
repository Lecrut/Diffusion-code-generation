from datetime import datetime

def get_year_delta(first: datetime, second: datetime) -> int:
    if first.year == second.year:
        return 0
    if first.year > second.year:
        return first.year - second.year
    return second.year - first.year

if __name__ == '__main__':
    start = datetime(2015, 6, 10)
    end = datetime(2020, 11, 25)
    print(get_year_delta(start, end))