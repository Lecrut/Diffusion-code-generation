from datetime import date

MONTHS_IN_YEAR = 12
DAYS_IN_COMMON_YEAR = 365
DAYS_IN_LEAP_YEAR = 366

def compute_year_difference(start: date, end: date) -> int:
    if start > end:
        return -compute_year_difference(end, start)
    
    years = end.year - start.year
    
    start_day_of_year = start.toordinal() - date(start.year, 1, 1).toordinal() + 1
    end_day_of_year = end.toordinal() - date(end.year, 1, 1).toordinal() + 1
    
    if end_day_of_year < start_day_of_year:
        years -= 1
        
    return years

if __name__ == '__main__':
    d_start = date(2019, 11, 2)
    d_end = date(2023, 11, 3)
    diff = compute_year_difference(d_start, d_end)
    print(diff)