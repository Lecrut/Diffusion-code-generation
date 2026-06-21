from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
MONTHS_IN_YEAR = 12

def calculate_year_span(start_date_str: str, end_date_str: str) -> int:
    date_start = datetime.strptime(start_date_str, DATE_FORMAT)
    date_end = datetime.strptime(end_date_str, DATE_FORMAT)
    
    year_diff = date_end.year - date_start.year
    
    if date_end.month < date_start.month:
        year_diff -= 1
    elif date_end.month == date_start.month:
        if date_end.day < date_start.day:
            year_diff -= 1
            
    return abs(year_diff)

if __name__ == '__main__':
    start = "2018-06-15"
    end = "2023-04-10"
    span = calculate_year_span(start, end)
    print(span)