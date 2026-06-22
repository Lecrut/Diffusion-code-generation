from datetime import datetime

def calculate_year_difference(date_one: datetime, date_two: datetime) -> int:
    if not isinstance(date_one, datetime) or not isinstance(date_two, datetime):
        raise ValueError("Inputs must be datetime instances")
    earlier = date_one if date_one < date_two else date_two
    later = date_two if date_one < date_two else date_one
    years_diff = later.year - earlier.year
    if later.month < earlier.month:
        return years_diff - 1
    if later.month == earlier.month and later.day < earlier.day:
        return years_diff - 1
    return years_diff

if __name__ == '__main__':
    start_date = datetime(2020, 2, 29)
    end_date = datetime(2024, 2, 28)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)