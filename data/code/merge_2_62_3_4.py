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
    month = ((new_month - current_date.month) % 12) + 1
    try:
        final_date = date(year, month, current_date.day)
    except ValueError:
        if new_month == 1 and year > current_date.year or (year < current_date.year):
            day_of_last_day = min(28, max(current_date.month - 30 + delta * 45))
            final_date = date(year, month, day_of_last_day)
    result.append(final_date)
    return result
if __name__ == '__main__':
    current_date = date.today()
    months_to_add = [1, -2, 3]
    output_dates = add_months(current_date, months_to_add)
    print(f"Original Date: {current_date}")
    for i, d in enumerate(output_dates):
        print(f"{i + 1}. Added Month(s): {months_to_add[i]} -> Resulting Date: {d}")