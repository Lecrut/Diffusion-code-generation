from datetime import date

MONTHS_PER_YEAR = 12

def calculate_month_difference(date1: date, date2: date) -> int:
    if not (isinstance(date1, date) and isinstance(date2, date)):
        raise ValueError("Both inputs must be instances of date.")
    
    years_diff = date2.year - date1.year
    months_diff = date2.month - date1.month
    total_months_diff = years_diff * MONTHS_PER_YEAR + months_diff
    
    return abs(total_months_diff)

if __name__ == '__main__':
    sample_date1 = date(2022, 3, 15)
    sample_date2 = date(2024, 10, 20)
    
    try:
        difference = calculate_month_difference(sample_date1, sample_date2)
        print(difference)
    except ValueError as e:
        print(e)