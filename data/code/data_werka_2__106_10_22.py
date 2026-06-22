from datetime import datetime

def get_absolute_year_difference(dt_a: datetime, dt_b: datetime) -> int:
    start_date = dt_a if dt_a < dt_b else dt_b
    end_date = dt_b if dt_a < dt_b else dt_a
    year_count = end_date.year - start_date.year
    current_date = start_date.replace(year=start_date.year + year_count)
    if current_date > end_date:
        year_count -= 1
    return year_count

if __name__ == '__main__':
    date_one = datetime(1995, 12, 31)
    date_two = datetime(2023, 1, 1)
    diff = get_absolute_year_difference(date_one, date_two)
    print(diff)