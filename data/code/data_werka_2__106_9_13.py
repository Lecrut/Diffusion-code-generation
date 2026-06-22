from datetime import date

def year_difference(date1: date, date2: date) -> int:
    d1 = date1 if date1 < date2 else date2
    d2 = date2 if date1 < date2 else date1
    years = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        years -= 1
    return years

if __name__ == '__main__':
    d1 = date(2020, 1, 1)
    d2 = date(2023, 12, 31)
    result = year_difference(d1, d2)
    print(result)