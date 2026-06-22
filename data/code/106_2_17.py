from datetime import datetime

def calculate_year_difference(start_date: datetime, end_date: datetime) -> int:
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    years = end_date.year - start_date.year
    if years > 0:
        try:
            anniversary = start_date.replace(year=end_date.year)
            if end_date < anniversary:
                years -= 1
        except ValueError:
            years -= 1
    return years

if __name__ == '__main__':
    start = datetime(2000, 2, 29)
    end = datetime(2023, 2, 28)
    result = calculate_year_difference(start, end)
    print(result)