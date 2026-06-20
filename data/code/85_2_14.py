from datetime import datetime, timedelta

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def difference_in_weeks(date1_str, date2_str):
    if not (is_valid_date(date1_str) and is_valid_date(date2_str)):
        raise ValueError("Both dates must be in the format YYYY-MM-DD.")
    
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    time_difference = abs(date1 - date2)
    weeks = time_difference.days / 7
    return int(weeks)

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2023-01-29'
    date_c = '2023-07-01'
    date_d = '2024-01-01'
    
    diff_ab = difference_in_weeks(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {diff_ab} weeks")
    
    diff_cd = difference_in_weeks(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {diff_cd} weeks")
    
    diff_ac = difference_in_weeks(date_a, date_c)
    print(f"Difference between {date_a} and {date_c}: {diff_ac} weeks")