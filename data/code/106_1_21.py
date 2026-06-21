import calendar
from datetime import date

def calculate_year_span(start_date_str: str, end_date_str: str) -> int:
    fmt = "%Y-%m-%d"
    parts1 = start_date_str.split("-")
    y1, m1, d1 = int(parts1[0]), int(parts1[1]), int(parts1[2])
    start = date(y1, m1, d1)
    
    parts2 = end_date_str.split("-")
    y2, m2, d2 = int(parts2[0]), int(parts2[1]), int(parts2[2])
    end = date(y2, m2, d2)
    
    if start > end:
        start, end = end, start
    
    years = end.year - start.year
    last_day_of_bday = calendar.monthrange(end.year, m1)[1]
    day = min(d1, last_day_of_bday)
    
    if end.month < m1 or (end.month == m1 and end.day < day):
        years -= 1
    
    return max(0, years)

if __name__ == '__main__':
    result = calculate_year_span("2000-02-28", "2024-02-27")
    print(result)