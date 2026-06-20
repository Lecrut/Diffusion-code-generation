from datetime import datetime

def date_difference(date1, date2):
    delta = abs((date1 - date2).days)
    years = delta // 365
    months = (delta % 365) // 30
    days = (delta % 365) % 30
    return f"{years} years, {months} months, and {days} days"

if __name__ == '__main__':
    date_a = datetime(2019, 7, 4)
    date_b = datetime(2023, 1, 1)
    result1 = date_difference(date_a, date_b)
    print(f"Difference between {date_a.date()} and {date_b.date()}: {result1}")
    
    date_c = datetime(2025, 12, 25)
    date_d = datetime(2023, 6, 15)
    result2 = date_difference(date_c, date_d)
    print(f"Difference between {date_c.date()} and {date_d.date()}: {result2}")
    
    date_e = datetime(2022, 9, 1)
    date_f = datetime(2023, 8, 31)
    result3 = date_difference(date_e, date_f)
    print(f"Difference between {date_e.date()} and {date_f.date()}: {result3}")