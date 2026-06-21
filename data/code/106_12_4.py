from datetime import date

def years_between(start: date, end: date) -> int:
    years = end.year - start.year
    if (end.month, end.day) < (start.month, start.day):
        years -= 1
    return years

if __name__ == '__main__':
    d1 = date(2000, 1, 1)
    d2 = date(2023, 12, 31)
    result = years_between(d1, d2)
    print(result)