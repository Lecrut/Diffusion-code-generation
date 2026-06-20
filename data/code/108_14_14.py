def validate_date_format(date_string: str) -> None:
    if not isinstance(date_string, str):
        raise TypeError("Date must be a string.")
    parts = date_string.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def get_day_of_month(date_string: str) -> int:
    validate_date_format(date_string)
    year, month, day = map(int, date_string.split('-'))
    return day

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")