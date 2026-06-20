from datetime import date

def get_next_month_start(input_date: date) -> date:
    if input_date.month == 12:
        next_month = 1
        next_year = input_date.year + 1
    else:
        next_month = input_date.month + 1
        next_year = input_date.year
    return date(next_year, next_month, 1)

if __name__ == '__main__':
    sample_dates = [date(2023, 10, 15), date(2024, 12, 31), date(2025, 1, 5)]
    for sample_date in sample_dates:
        result = get_next_month_start(sample_date)
        print(f"Input: {sample_date}, Output: {result}")