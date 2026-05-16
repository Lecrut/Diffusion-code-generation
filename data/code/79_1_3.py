from datetime import date, timedelta
def get_next_month_date(input_date: date) -> date:
    if input_date.month == 12:
        next_month = 1
        next_year = input_date.year + 1
    else:
        next_month = input_date.month + 1
        next_year = input_date.year
    return date(next_year, next_month, 1)
if __name__ == '__main__':
    date1 = date(2023, 10, 15)
    result1 = get_next_month_date(date1)
    print(f"Input: {date1}, Next Month Start: {result1}")
    date2 = date(2024, 12, 31)
    result2 = get_next_month_date(date2)
    print(f"Input: {date2}, Next Month Start: {result2}")
    date3 = date(2025, 1, 5)
    result3 = get_next_month_date(date3)
    print(f"Input: {date3}, Next Month Start: {result3}")