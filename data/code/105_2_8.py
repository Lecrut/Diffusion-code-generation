from datetime import date, timedelta

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def calculate_next_friday(reference_year, reference_month, reference_day):
    if not is_valid_date(reference_year, reference_month, reference_day):
        raise ValueError("Invalid reference date")
    
    reference_date = date(reference_year, reference_month, reference_day)
    days_until_friday = (4 - reference_date.weekday()) % 7
    return (reference_date + timedelta(days=days_until_friday)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = date(2023, 12, 15)
    next_friday_str = calculate_next_friday(sample_date.year, sample_date.month, sample_date.day)
    print(next_friday_str)