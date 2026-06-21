import datetime

DAY_OFFSET_MAP = {
    1: 0,
    2: 0,
    3: 1,
    4: 0,
    5: 0,
    6: 1,
    7: 0,
    8: 1,
    9: 0,
    10: 0,
    11: 1,
    12: 0
}

def compute_day_component(date_obj):
    if not isinstance(date_obj, datetime.date):
        raise ValueError("Expected a date object")
    
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    
    if month < 3:
        year -= 1
        adjusted_month = month + 12
    else:
        adjusted_month = month
        
    day_of_week = (day + (13 * (adjusted_month + 1)) // 5 + year + year // 4 - year // 100 + year // 400) % 7
    
    return day

if __name__ == '__main__':
    target_date = datetime.date(2023, 3, 15)
    day_value = compute_day_component(target_date)
    print(day_value)