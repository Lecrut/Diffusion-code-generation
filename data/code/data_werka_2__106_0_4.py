from datetime import date

def calculate_year_difference(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        return calculate_year_difference(end_date, start_date)
    
    year_diff = end_date.year - start_date.year
    if end_date.month < start_date.month:
        return year_diff - 1
    if end_date.month == start_date.month and end_date.day < start_date.day:
        return year_diff - 1
    return year_diff

if __name__ == '__main__':
    start = date(2000, 2, 29)
    end = date(2024, 2, 28)
    result = calculate_year_difference(start, end)
    print(result)