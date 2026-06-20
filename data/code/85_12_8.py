from datetime import datetime, timedelta

def calculate_week_difference(date1: datetime, date2: datetime) -> int:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Inputs must be datetime objects")
    
    time_difference = abs(date1 - date2)
    full_weeks = time_difference.days // 7
    return full_weeks

if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 15)
    diff_ab = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {diff_ab} weeks")
    
    date_c = datetime(2023, 6, 1)
    date_d = datetime(2023, 6, 20)
    diff_cd = calculate_week_difference(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {diff_cd} weeks")
    
    date_e = datetime(2024, 1, 1)
    date_f = datetime(2023, 1, 1)
    diff_ef = calculate_week_difference(date_e, date_f)
    print(f"Difference between {date_e.date()} and {date_f.date()}: {diff_ef} weeks")