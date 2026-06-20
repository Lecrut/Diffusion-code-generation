def get_day_of_month(date_string: str) -> int:
    year = int(date_string[:4])
    month = int(date_string[5:7])
    day = int(date_string[8:])
    
    if not (1 <= month <= 12):
        raise ValueError("Invalid month. Month must be between 1 and 12.")
    if not (1 <= day <= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]):
        raise ValueError("Invalid day for the given month.")
    
    return day

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")