from datetime import date

def calculate_absolute_year_difference(first_date: date, second_date: date) -> int:
    if not isinstance(first_date, date) or not isinstance(second_date, date):
        raise ValueError("Inputs must be date objects")
    delta = first_date - second_date
    total_days = abs(delta.days)
    year_count = total_days // 365
    return year_count

if __name__ == '__main__':
    start = date(2015, 6, 15)
    end = date(2022, 11, 20)
    diff = calculate_absolute_year_difference(start, end)
    print(diff)