def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def get_day_of_month(date_string):
    year = int(date_string[:4])
    month = int(date_string[5:7])
    day = int(date_string[8:])
    
    if not (1 <= month <= 12 and 1 <= day <= days_in_month(year, month)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    return day

if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    
    print(f"Day of month for {sample_date_1}: {get_day_of_month(sample_date_1)}")
    print(f"Day of month for {sample_date_2}: {get_day_of_month(sample_date_2)}")
    print(f"Day of month for {sample_date_3}: {get_day_of_month(sample_date_3)}")