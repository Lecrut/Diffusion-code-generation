import re

def get_day_of_month(date_str):
    if not isinstance(date_str, str) or len(date_str) != 10:
        raise ValueError("Invalid date format")
    
    match = re.match(r'^\d{4}-\d{2}-\d{2}$', date_str)
    if not match:
        raise ValueError("Invalid date format")
    
    day = int(date_str.split('-')[2])
    return day

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    result1 = get_day_of_month(sample_date1)
    print(f"Date: {sample_date1}, Day of the month: {result1}")
    
    sample_date2 = "2023-12-25"
    result2 = get_day_of_month(sample_date2)
    print(f"Date: {sample_date2}, Day of the month: {result2}")