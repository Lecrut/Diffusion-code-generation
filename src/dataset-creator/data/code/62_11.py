from datetime import date
def add_months(d: date, n: int) -> date:
    year = d.year + (d.month - 1 + n) // 12
    month = (d.month - 1 + n) % 12 + 1
    day = min(d.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)
if __name__ == '__main__':
    current_date = "2024-02-29"
    months_to_add = 5
    result_date = add_months(date.fromisoformat(current_date), months_to_add)
    print(result_date.isoformat())