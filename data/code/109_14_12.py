import datetime

def days_until_end_of_month(year: int, month: int) -> str:
    try:
        target_date = datetime.date(year, month, 1)
        if month == 12:
            next_month_start = datetime.date(year + 1, 1, 1)
        else:
            next_month_start = datetime.date(year, month + 1, 1)
        
        days_in_current_month = (next_month_start - target_date).days
        return f"Month: {month}, Year: {year}\nDays left until the end of the month: {days_in_current_month}"
    
    except ValueError as e:
        return f"Error: Invalid date provided. {e}"

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    print(days_until_end_of_month(sample_year, sample_month))