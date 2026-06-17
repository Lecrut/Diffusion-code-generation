from datetime import date
def add_months(d: date, months: int) -> date:
    year = d.year + (d.month - 1 + months) // 12
    month = ((d.month - 1 + months) % 12) + 1
    day = min(d.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)
if __name__ == '__main__':
    start_date = date(2024, 5, 15)
    months_to_add = 7
    result_date = add_months(start_date, months_to_add)
    print(result_date.strftime("%Y-%m-%d"))