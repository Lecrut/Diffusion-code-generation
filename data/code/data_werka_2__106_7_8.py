from datetime import date

def calculate_full_years(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    if start_date == end_date:
        return 0
    year_count = end_date.year - start_date.year - 1
    anniversary = date(end_date.year, start_date.month, start_date.day)
    if end_date >= anniversary:
        year_count += 1
    return year_count

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = calculate_full_years(start, end)
    print(result)