from datetime import date

def count_full_years_between(start: date, end: date) -> int:
    if start > end:
        raise ValueError("start must be before or equal to end")
    if start == end:
        return 0
    full_years = end.year - start.year - 1
    next_birthday = date(end.year, start.month, start.day)
    if next_birthday <= end:
        full_years += 1
    return full_years

if __name__ == '__main__':
    start_date = date(2000, 2, 28)
    end_date = date(2024, 3, 1)
    years_passed = count_full_years_between(start_date, end_date)
    print(years_passed)