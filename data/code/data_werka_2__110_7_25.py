from datetime import datetime
import calendar

def parse_date_string(date_str):
    if not isinstance(date_str, str):
        raise TypeError("Input must be a string")
    components = date_str.split('-')
    if len(components) != 3:
        raise ValueError(f"Expected MM-DD-YYYY format, got {date_str}")
    month_str, day_str, year_str = components
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        raise ValueError(f"Non-numeric components in {date_str}")
    if len(year_str) != 4:
        raise ValueError(f"Year must be 4 digits in {date_str}")
    
    month_val = int(month_str)
    day_val = int(day_str)
    year_val = int(year_str)
    
    if not (1 <= month_val <= 12):
        raise ValueError(f"Invalid month {month_val} in {date_str}")
    
    max_days = calendar.monthrange(year_val, month_val)[1]
    if not (1 <= day_val <= max_days):
        raise ValueError(f"Invalid day {day_val} for month {month_val} in {date_str}")
        
    return datetime(year_val, month_val, day_val)

def sort_dates_chronologically(date_list):
    if not isinstance(date_list, list):
        raise TypeError("Input must be a list")
    
    validated_dates = []
    for d in date_list:
        dt_obj = parse_date_string(d)
        validated_dates.append((dt_obj, d))
    
    validated_dates.sort(key=lambda item: item[0])
    
    return [item[1] for item in validated_dates]

if __name__ == '__main__':
    sample_dates = [
        '12-25-2023',
        '01-01-2023',
        '02-29-2024',
        '10-15-2022',
        '06-30-2023'
    ]
    sorted_result = sort_dates_chronologically(sample_dates)
    print(sorted_result)