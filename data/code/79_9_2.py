from datetime import date, timedelta
def get_next_month_start(input_date: date) -> date:
    if input_date.month == 12:
        next_month = 1
        next_year = input_date.year + 1
    else:
        next_month = input_date.month + 1
        next_year = input_date.year
    return date(next_year, next_month, 1)
if __name__ == '__main__':
    sample_date1 = date(2023, 10, 15)
    result1 = get_next_month_start(sample_date1)
    print(f"Input: {sample_date1}, Result: {result1}")
    sample_date2 = date(2023, 12, 31)
    result2 = get_next_month_start(sample_date2)
    print(f"Input: {sample_date2}, Result: {result2}")
    sample_date3 = date(2024, 1, 5)
    result3 = get_next_month_start(sample_date3)
    print(f"Input: {sample_date3}, Result: {result3}")
    sample_date4 = date(2025, 5, 20)
    result4 = get_next_month_start(sample_date4)
    print(f"Input: {sample_date4}, Result: {result4}")