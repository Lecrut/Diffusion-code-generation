from datetime import datetime

def date_difference(date1, date2):
    delta = abs((date1 - date2).days)
    years = delta // 365
    months = (delta % 365) // 30
    days = (delta % 365) % 30
    return f"{years} years, {months} months, and {days} days"

if __name__ == '__main__':
    date_a = datetime(2023, 1, 1)
    date_b = datetime(2023, 1, 10)
    print(date_difference(date_a, date_b))
    
    date_c = datetime(2024, 5, 15)
    date_d = datetime(2024, 4, 1)
    print(date_difference(date_c, date_d))
    
    date_e = datetime(2022, 12, 31)
    date_f = datetime(2023, 1, 1)
    print(date_difference(date_e, date_f))