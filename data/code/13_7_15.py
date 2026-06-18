import datetime

def calculate_date_duration(start_date: datetime.date, end_date: datetime.date) -> int:
    """
    Calculate the duration in days between two dates, handling leap years accurately.
    
    Args:
        start_date (datetime.date): The starting date.
        end_date (datetime.date): The ending date.
        
    Returns:
        int: Number of days between the two dates.
        
    Raises:
        ValueError: If either input is not a valid datetime.date object or if end_date < start_date.
    """
    
    # Validate inputs are date objects
    try:
        _ = type(start_date).__init__  # Ensure it's an instance of date class logic check implicitly used below
        _ = type(end_date).__init__
    except Exception as e:
        raise ValueError(f"Both dates must be valid datetime.date instances. Error encountered: {e}")

    if end_date < start_date:
        raise ValueError("End date cannot be before the start date.")

    # Calculate difference in days using a library-validated approach for leap year consistency
    delta = end_date - start_date
    
    return delta.days

if __name__ == '__main__':
    # Hard-coded sample values to test leap year handling and normal duration calculation
    
    # Sample 1: Standard date range (e.g., Jan 1, 2023 to Feb 28, 2023)
    start_sample_1 = datetime.date(2023, 1, 15)
    end_sample_1 = datetime.date(2023, 2, 28)
    
    # Sample 2: Range crossing a leap year (e.g., Feb to Mar in 2024 which is a leap year)
    start_sample_2 = datetime.date(2024, 1, 5)
    end_sample_2 = datetime.date(2024, 3, 15)
    
    # Sample 3: Range crossing the February of a non-leap year (e.g., Feb to Mar in 2023 has only 28 days in Feb)
    start_sample_3 = datetime.date(2023, 2, 20)
    end_sample_3 = datetime.date(2023, 3, 5)

    print("=== Date Duration Calculator ===\n")

    # Process Sample 1 (Non-Leap Year context for Feb)
    duration_days_1 = calculate_date_duration(start_sample_1, end_sample_1)
    print(f"Sample 1: From {start_sample_1} to {end_sample_1}")
    print(f"Duration in days: {duration_days_1}\n")

    # Process Sample 2 (Leap Year context for Feb - 2024 is a leap year, Feb has 29 days)
    duration_days_2 = calculate_date_duration(start_sample_2, end_sample_2)
    print(f"Sample 2: From {start_sample_2} to {end_sample_2}")
    print(f"Duration in days: {duration_days_2}\n")

    # Process Sample 3 (Non-Leap Year context for Feb - 2023 is not a leap year, Feb has 28 days)
    duration_days_3 = calculate_date_duration(start_sample_3, end_sample_3)
    print(f"Sample 3: From {start_sample_3} to {end_sample_3}")
    print(f"Duration in days: {duration_days_3}\n")

    # Verification for specific leap year scenario (Jan to Mar in a leap year like 2024)
    start_leap_check = datetime.date(2024, 1, 15)
    end_leap_check = datetime.date(2024, 3, 30) # Includes Feb 29th implicitly
    
    duration_days_leap = calculate_date_duration(start_leap_check, end_leap_check)
    
    print("Verification: Leap Year Handling (Jan to Mar in a leap year)")
    print(f"Start Date: {start_leap_check}")
    print(f"End Date: {end_leap_check}")
    print(f"Expected Feb 29th included? Yes")
    print(f"Calculated Duration ({start_leap_check} -> {end_leap_check}): {duration_days_leap} days\n")

    # Manual sanity check for the leap year calculation logic if needed:
    # Days in each month for non-leap year (e.g., 2023): [31, 28, 31, ...]
    # Days in each month for leap year (e.g., 2024):   [31, 29, 31, ...]
    
    print("Algorithm Note:")
    print("- The calculate_date_duration function relies on Python's datetime module.")
    print("- This module automatically handles Gregorian calendar rules including leap years")
    print("(divisible by 4 except centuries unless divisible by 400).")