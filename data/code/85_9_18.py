import datetime

def date_to_week_number(date_str):
    year, month, day = map(int, date_str.split('-'))
    return (year - 1970) * 52 + (month - 1) * 4 + (day // 7)

def calculate_week_difference(date1, date2):
    week1 = date_to_week_number(date1)
    week2 = date_to_week_number(date2)
    return abs(week1 - week2)

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2023-01-10'
    result1 = calculate_week_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1} weeks")
    
    date_c = '2023-01-10'
    date_d = '2022-01-01'
    result2 = calculate_week_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2} weeks")
    
    date_e = '2024-05-01'
    date_f = '2024-04-01'
    result3 = calculate_week_difference(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3} weeks")