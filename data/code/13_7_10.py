import datetime

def calculate_date_duration(start_date: str, end_date: str) -> int:
    """
    Calculates the duration in days between two dates provided as ISO format strings (YYYY-MM-DD).
    
    Args:
        start_date (str): Start date string in 'YYYY-MM-DD' format.
        end_date (str): End date string in 'YYYY-MM-DD' format.
        
    Returns:
        int: The number of days between the two dates.
    """
    try:
        # Parse input strings to datetime objects using fromisoformat for robustness on standard formats
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        
        # Calculate the difference in days. 
        # Using timedelta ensures accurate calculation regardless of leap years because 
        # Python's datetime handles calendar rules internally during arithmetic operations.
        delta = end - start
        
        return delta.days

    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD'. Error details: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    # Sample 1: Includes a leap year (2024) between the dates.
    start_date_1 = "2023-01-01"
    end_date_1 = "2024-01-01"

    # Sample 2: Crosses multiple years including another leap year (2028).
    start_date_2 = "2020-06-15"
    end_date_2 = "2023-07-14"

    sample_cases = [
        {"start": start_date_1, "end": end_date_1},
        {"start": start_date_2, "end": end_date_2}
    ]

    for i, case in enumerate(sample_cases):
        duration_days = calculate_date_duration(case["start"], case["end"])
        print(f"Duration from {case['start']} to {case['end']}: {duration_days} days")