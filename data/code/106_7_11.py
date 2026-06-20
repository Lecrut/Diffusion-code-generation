from datetime import date

def years_between_dates(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("Start date must be before end date.")
    
    year_diff = end_date.year - start_date.year
    
    if (start_date.month, start_date.day) > (end_date.month, end_date.day):
        year_diff -= 1
    
    return year_diff

if __name__ == '__main__':
    start = date(2015, 3, 1)
    end = date(2024, 2, 29)
    print(years_between_dates(start, end))