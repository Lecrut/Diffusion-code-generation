from datetime import date

def calculate_year_difference(start_date: date, end_date: date) -> int:
    years = end_date.year - start_date.year
    if end_date.month < start_date.month:
        years -= 1
    elif end_date.month == start_date.month:
        if end_date.day < start_date.day:
            years -= 1
    return years

if __name__ == '__main__':
    start = date(2000, 1, 1)
    end = date(2023, 12, 31)
    result = calculate_year_difference(start, end)
    print(result)