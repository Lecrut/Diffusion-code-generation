import datetime

def calculate_week_difference(date1, date2):
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise ValueError("Both arguments must be datetime objects")
    
    diff = abs(date1 - date2)
    weeks = diff.days // 7
    return weeks

if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 1, 10, 0, 0)
    date_b = datetime.datetime(2023, 1, 15, 14, 30, 0)
    result1 = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1} weeks")
    
    date_c = datetime.datetime(2023, 1, 1)
    date_d = datetime.datetime(2023, 1, 8)
    result2 = calculate_week_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2} weeks")
    
    date_e = datetime.datetime(2022, 12, 31)
    date_f = datetime.datetime(2023, 1, 2)
    result3 = calculate_week_difference(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3} weeks")