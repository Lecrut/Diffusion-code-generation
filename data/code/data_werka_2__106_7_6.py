from datetime import date

def calculate_full_years(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    
    years = end_date.year - start_date.year
    
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
        
    return years

if __name__ == '__main__':
    start = date(2000, 2, 29)
    end = date(2024, 2, 28)
    result = calculate_full_years(start, end)
    print(result)