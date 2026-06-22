from datetime import datetime

def get_year_span(reference: datetime, current: datetime) -> int:
    if reference > current:
        raise ValueError("Reference date must be before or equal to current date")
    
    span = current.year - reference.year
    
    if span > 0:
        reference_anniversary = reference.replace(year=current.year)
        if current < reference_anniversary:
            span -= 1
            
    return span

if __name__ == '__main__':
    start_date = datetime(1990, 5, 10)
    end_date = datetime(2023, 5, 9)
    years = get_year_span(start_date, end_date)
    print(years)