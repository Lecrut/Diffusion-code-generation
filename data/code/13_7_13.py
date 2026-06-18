import datetime

def calculate_duration_between_dates(date1: datetime.date, date2: datetime.date) -> int:
    """
    Calculate the duration in days between two dates, accurately handling leap years.
    
    Parameters:
        date1 (datetime.date): The start date.
        date2 (datetime.date): The end date.
        
    Returns:
        int: The number of days between date1 and date2.
            If date2 is before date1, returns a negative value representing the duration backwards.
    
    Raises:
        ValueError: If either input is not a valid date object.
    """
    if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
        raise ValueError("Both inputs must be instances of datetime.date")

    # Ensure we are calculating forward (date2 - date1), but preserve sign for backward dates
    delta = date2 - date1
    
    return delta.days

if __name__ == '__main__':
    # Sample values with hardcoded test cases including leap years
    sample_dates = [
        datetime.date(2023, 5, 15),      # Start: May 15, 2023
        datetime.date(2024, 5, 15),      # End: May 15, 2024 (Leap year involved)
    ]

    start_date = sample_dates[0]
    end_date = sample_dates[1]

    duration_days = calculate_duration_between_dates(start_date, end_date)
    
    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Duration in days (forward): {duration_days}")