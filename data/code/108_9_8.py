from typing import Tuple

def get_day_of_month(date_tuple: Tuple[int, int, int]) -> int:
    if not isinstance(date_tuple, tuple) or len(date_tuple) != 3:
        raise ValueError("Input must be a tuple of three integers (year, month, day)")
    
    year, month, day = date_tuple
    if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
        raise ValueError("All elements in the tuple must be integers")
    
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    
    return day

if __name__ == '__main__':
    sample_date_1 = (2023, 10, 27)
    result_1 = get_day_of_month(sample_date_1)
    print(f"Day of the month for {sample_date_1}: {result_1}")
    
    sample_date_2 = (1999, 1, 1)
    result_2 = get_day_of_month(sample_date_2)
    print(f"Day of the month for {sample_date_2}: {result_2}")
    
    sample_date_3 = (2024, 2, 29)
    result_3 = get_day_of_month(sample_date_3)
    print(f"Day of the month for {sample_date_3}: {result_3}")