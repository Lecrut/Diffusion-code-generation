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
    sample_date_1 = date(2023, 10, 15)
    result_1 = get_next_month_start(sample_date_1)
    print(f"Input: {sample_date_1}, Output: {result_1}")
    sample_date_2 = date(2023, 12, 31)
    result_2 = get_next_month_start(sample_date_2)
    print(f"Input: {sample_date_2}, Output: {result_2}")
    sample_date_3 = date(2024, 1, 5)
    result_3 = get_next_month_start(sample_date_3)
    print(f"Input: {sample_date_3}, Output: {result_3}")
    sample_date_4 = date(2025, 5, 20)
    result_4 = get_next_month_start(sample_date_4)
    print(f"Input: {sample_date_4}, Output: {result_4}")