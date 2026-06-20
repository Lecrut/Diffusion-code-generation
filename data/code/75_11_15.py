from datetime import datetime

def date_difference(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    delta = abs((date2 - date1).days)
    years, remainder = divmod(delta, 365)
    months, days = divmod(remainder, 30)
    
    return f"{years} year(s), {months} month(s), and {days} day(s)"

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2024-05-15"
    result1 = date_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1}")
    
    date_c = "2024-05-15"
    date_d = "2024-04-01"
    result2 = date_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2}")
    
    date_e = "2022-12-31"
    date_f = "2023-01-01"
    result3 = date_difference(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3}")