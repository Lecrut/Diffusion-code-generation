def get_day_of_month(date_string: str) -> int:
    year, month, day = map(int, date_string.split('-'))
    if month < 1 or month > 12:
        raise ValueError("Invalid month. Month must be between 1 and 12.")
    return day

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")