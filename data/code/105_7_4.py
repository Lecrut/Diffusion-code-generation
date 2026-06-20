from datetime import datetime, timedelta

def get_upcoming_tuesday(start_date: datetime) -> datetime:
    if not isinstance(start_date, datetime):
        raise ValueError("Invalid input: start_date must be an instance of datetime.")
    
    days_until_tuesday = (1 + 6 - start_date.weekday()) % 7
    upcoming_tuesday = start_date + timedelta(days=days_until_tuesday)
    return upcoming_tuesday

if __name__ == '__main__':
    reference_date = datetime(2023, 7, 4)
    try:
        result = get_upcoming_tuesday(reference_date)
        print(result.strftime('%Y-%m-%d'))
    except ValueError as e:
        print(e)