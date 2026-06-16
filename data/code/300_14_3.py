from datetime import date
def days_until_month_end(full_date):
    year = full_date.year
    month = full_date.month
    if month == 12:
        return 0
    next_month = month + 1
    if next_month > 12:
        next_month = 1
        year += 1
    first_day_of_next_month = date(year, next_month, 1)
    days_in_current_month = (date(year, month + 1, 1) - date(year, month, 1)).days
    return (date(year, month + 1, 1) - full_date).days
if __name__ == '__main__':
    sample_date_1 = date(2023, 10, 15)
    result_1 = days_until_month_end(sample_date_1)
    print(f"Date: {sample_date_1}, Days remaining until end of month: {result_1}")
    sample_date_2 = date(2024, 1, 5)
    result_2 = days_until_month_end(sample_date_2)
    print(f"Date: {sample_date_2}, Days remaining until end of month: {result_2}")
    sample_date_3 = date(2025, 12, 20)
    result_3 = days_until_month_end(sample_date_3)
    print(f"Date: {sample_date_3}, Days remaining until end of month: {result_3}")
    sample_date_4 = date(2026, 5, 1)
    result_4 = days_until_month_end(sample_date_4)
    print(f"Date: {sample_date_4}, Days remaining until end of month: {result_4}")