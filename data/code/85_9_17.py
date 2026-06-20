import datetime

def validate_date_format(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Date must be in 'YYYY-MM-DD' format")

def calculate_week_difference(date1_str, date2_str):
    date1 = validate_date_format(date1_str)
    date2 = validate_date_format(date2_str)
    delta = abs(date1 - date2)
    weeks = delta.days // 7
    return weeks

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2023-01-15'
    result1 = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1} weeks")
    
    date_c = '2023-01-15'
    date_d = '2022-01-01'
    result2 = calculate_week_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2} weeks")
    
    date_e = '2024-05-01'
    date_f = '2024-04-01'
    result3 = calculate_week_difference(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3} weeks")