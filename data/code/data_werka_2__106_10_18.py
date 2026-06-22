from datetime import datetime

def get_full_year_difference(dt_a: datetime, dt_b: datetime) -> int:
    start_date = dt_a if dt_a < dt_b else dt_b
    end_date = dt_b if dt_a < dt_b else dt_a
    year_diff = end_date.year - start_date.year
    current_anniversary = start_date.replace(year=end_date.year)
    if current_anniversary > end_date:
        year_diff -= 1
    return year_diff

if __name__ == '__main__':
    date_a = datetime(1990, 5, 15)
    date_b = datetime(2023, 4, 10)
    diff = get_full_year_difference(date_a, date_b)
    print(diff)