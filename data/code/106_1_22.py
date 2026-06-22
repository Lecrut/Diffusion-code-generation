from datetime import date

def get_year_difference(start_date: str, end_date: str) -> int:
    d_start = date.fromisoformat(start_date)
    d_end = date.fromisoformat(end_date)
    
    if d_start > d_end:
        d_start, d_end = d_end, d_start
        
    years = d_end.year - d_start.year
    
    if d_end.month < d_start.month:
        years -= 1
    elif d_end.month == d_start.month and d_end.day < d_start.day:
        years -= 1
        
    return years

if __name__ == '__main__':
    print(get_year_difference("2020-02-29", "2023-03-01"))