from datetime import date

def _validate_date_input(year: int, month: int, day: int) -> date:
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("Year, month, and day must be integers")
    try:
        return date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {year}-{month}-{day}") from e

def calculate_year_difference(year1: int, month1: int, day1: int, year2: int, month2: int, day2: int) -> int:
    d1 = _validate_date_input(year1, month1, day1)
    d2 = _validate_date_input(year2, month2, day2)
    
    if d1 > d2:
        d1, d2 = d2, d1
        
    years = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        years -= 1
        
    return years

if __name__ == '__main__':
    result = calculate_year_difference(1990, 5, 15, 2023, 10, 15)
    print(result)