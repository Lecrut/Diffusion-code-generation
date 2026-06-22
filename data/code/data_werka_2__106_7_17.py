from datetime import date

def calculate_full_years(start_date: date, end_date: date) -> int:
    years = end_date.year - start_date.year
    if (end_date.month, end_date.day) < (start_date.month, start_date.day):
        years -= 1
    return years

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = calculate_full_years(start, end)
    print(result)