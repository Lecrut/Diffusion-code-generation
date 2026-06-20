def get_day_of_month(date_string: str) -> int:
    year, month, day = map(int, date_string.split('-'))
    if not (1 <= month <= 12):
        raise ValueError("Invalid month. Please use 01-12.")
    if not (1 <= day <= 31):
        raise ValueError("Invalid day. Please use 01-31.")
    return day

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")