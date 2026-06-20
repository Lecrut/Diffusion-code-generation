def is_valid_date(year: int, month: int, day: int) -> bool:
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2 and (day > 29 or (year % 4 != 0 and day == 29)):
        return False
    return True

def get_day_of_month(date_string: str) -> int:
    year, month, day = map(int, date_string.split('-'))
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    return day

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")