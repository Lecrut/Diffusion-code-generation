from datetime import date, timedelta
def add_months(current_date: date, months_to_add: list[int]) -> list[date]:
    result = []
    for delta in months_to_add:
        new_year = current_date.year + (delta // 12)
        remaining_months = delta % 12
        new_month = current_date.month - 1 + remaining_months
        while new_month <= 0:
            new_month += 12
            new_year -= 1
        new_day = min(current_date.day, (date(new_year, new_month, 31).day))
        result.append(date(new_year, new_month, new_day))
    return result
if __name__ == '__main__':
    sample_date = date(2024, 5, 15)
    increments = [1, -6, 8]
    output_dates = add_months(sample_date, increments)
    print(output_dates)