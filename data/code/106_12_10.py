from datetime import date

def calculate_years_between(date1: date, date2: date) -> int:
    delta = abs(date2 - date1)
    years = delta.days // 365
    days_in_full_years = years * 365
    remaining_days = delta.days - days_in_full_years
    if (date2.month, date2.day) >= (date1.month, date1.day):
        years += remaining_days > 0
    else:
        years -= remaining_days > 0 and date2.year != date1.year
    return years

if __name__ == '__main__':
    d1 = date(2005, 6, 15)
    d2 = date(2023, 9, 20)
    print(calculate_years_between(d1, d2))