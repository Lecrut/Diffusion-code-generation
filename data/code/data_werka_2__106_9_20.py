from datetime import date

def year_difference(date1: date, date2: date) -> int:
    y1 = date1.year
    y2 = date2.year
    diff = y2 - y1
    if (date2.month, date2.day) < (date1.month, date1.day):
        diff -= 1
    return diff

if __name__ == '__main__':
    d1 = date(2020, 1, 1)
    d2 = date(2023, 12, 31)
    result = year_difference(d1, d2)
    print(result)