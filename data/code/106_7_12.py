from datetime import date

def get_full_years(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    if start_date == end_date:
        return 0
    years = end_date.year - start_date.year
    anniversary = date(end_date.year, start_date.month, start_date.day)
    if anniversary > end_date:
        years -= 1
    return years

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = get_full_years(start, end)
    print(result)