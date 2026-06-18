from datetime import date, timedelta
def add_months(current_date: date, months_to_add: list[int]) -> list[date]:
    result = []
    for delta in months_to_add:
        new_month = current_date.month + delta
        while True:
            if 1 <= new_month <= 12:
                break
            else:
                new_month -= 12
    year = current_date.year + (new_month - current_date.month) // 12
    month = ((current_date.month - 1 + delta) % 12) + 1 if delta >= 0 else ((current_date.month - 1 + delta) % 12) + 1
    day = min(current_date.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    result.append(date(year, month, day))
if __name__ == '__main__':
    current_date = date(2024, 5, 15)
    months_to_add = [1, 6, 12]
    print(add_months(current_date, months_to_add))