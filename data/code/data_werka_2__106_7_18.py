from datetime import date

def calculate_full_years(start: date, end: date) -> int:
    if start > end:
        raise ValueError("start must be before or equal to end")
    years = end.year - start.year
    if (end.month, end.day) < (start.month, start.day):
        years -= 1
    return years

if __name__ == '__main__':
    start_date = date(1990, 5, 15)
    end_date = date(2023, 5, 14)
    result = calculate_full_years(start_date, end_date)
    print(result)