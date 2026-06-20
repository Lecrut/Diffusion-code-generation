from datetime import date

def is_valid_date(year: int, month: int, day: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def calculate_day_of_year(input_date: str) -> int:
    input_format = "%Y-%m-%d"
    if not is_valid_date(*map(int, input_date.split('-'))):
        raise ValueError("Invalid date format or value")
    
    year, month, day = map(int, input_date.split('-'))
    return date(year, month, day).timetuple().tm_yday

if __name__ == '__main__':
    sample_date_1 = "2023-04-10"
    result_1 = calculate_day_of_year(sample_date_1)
    print(f"Date: {sample_date_1}, Day of Year: {result_1}")
    
    sample_date_2 = "2023-12-31"
    result_2 = calculate_day_of_year(sample_date_2)
    print(f"Date: {sample_date_2}, Day of Year: {result_2}")
    
    sample_date_3 = "2024-01-01"
    result_3 = calculate_day_of_year(sample_date_3)
    print(f"Date: {sample_date_3}, Day of Year: {result_3}")