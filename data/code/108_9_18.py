import datetime

def validate_date_tuple(date_tuple):
    if not isinstance(date_tuple, tuple) or len(date_tuple) != 3:
        raise ValueError("Input must be a tuple of three integers (year, month, day).")
    year, month, day = date_tuple
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise ValueError("All elements in the tuple must be integers.")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")
    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31.")

def get_day_of_month(date_tuple):
    validate_date_tuple(date_tuple)
    return date_tuple[2]

if __name__ == '__main__':
    sample_date_1 = (2023, 10, 27)
    day_1 = get_day_of_month(sample_date_1)
    print(f"Day of the month for {sample_date_1}: {day_1}")
    
    sample_date_2 = (1999, 1, 1)
    day_2 = get_day_of_month(sample_date_2)
    print(f"Day of the month for {sample_date_2}: {day_2}")
    
    sample_date_3 = (2024, 2, 29)
    day_3 = get_day_of_month(sample_date_3)
    print(f"Day of the month for {sample_date_3}: {day_3}")