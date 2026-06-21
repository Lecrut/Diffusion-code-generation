from datetime import date
from operator import sub

def get_year_distance(start: date, end: date) -> int:
    if start > end:
        return -get_year_distance(end, start)
    if start == end:
        return 0
    years = end.year - start.year
    anniversary = start.replace(year=end.year)
    if end < anniversary:
        return years - 1
    return years

if __name__ == '__main__':
    start_date = date(2020, 3, 1)
    end_date = date(2023, 2, 28)
    print(get_year_distance(start_date, end_date))