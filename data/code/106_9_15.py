from datetime import date

def year_difference(date1: date, date2: date) -> int:
    y1 = date1.year
    y2 = date2.year
    if date1.month < date2.month:
        return y2 - y1
    if date1.month > date2.month:
        return y2 - y1 - 1
    if date1.day <= date2.day:
        return y2 - y1
    return y2 - y1 - 1

if __name__ == '__main__':
    d1 = date(2020, 5, 15)
    d2 = date(2023, 5, 14)
    result = year_difference(d1, d2)
    print(result)