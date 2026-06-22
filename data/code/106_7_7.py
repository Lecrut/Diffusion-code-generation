from datetime import date

def get_full_years_elapsed(start: date, end: date) -> int:
    if start > end:
        raise ValueError("start must be before or equal to end")
    year_diff = end.year - start.year
    anniversary_date = date(end.year, start.month, start.day)
    if anniversary_date > end:
        return year_diff - 1
    return year_diff

if __name__ == '__main__':
    start_date = date(1985, 12, 31)
    end_date = date(2024, 1, 1)
    years = get_full_years_elapsed(start_date, end_date)
    print(years)