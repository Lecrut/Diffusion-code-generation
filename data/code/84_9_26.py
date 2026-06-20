from datetime import date

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    else:
        return 29 if is_leap_year(year) else 28

def calculate_day_of_year(date_obj):
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    if not (1 <= month <= 12 and 1 <= day <= days_in_month(month, year)):
        raise ValueError("Invalid date")
    
    return sum(days_in_month(m, year) for m in range(1, month)) + day

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(f"Date: {sample_date} -> Day of Year: {calculate_day_of_year(sample_date)}")