def validate_date_tuple(d):
    if not isinstance(d, tuple):
        raise ValueError("Input must be a tuple")
    if len(d) != 3:
        raise ValueError("Tuple must contain exactly three elements (year, month, day)")
    year, month, day = d
    if not all(isinstance(x, int) for x in d):
        raise ValueError("All elements must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1:
        raise ValueError("Day must be positive")
    days_in_months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    max_day = days_in_months[month]
    if month == 2 and is_leap:
        max_day = 29
    if day > max_day:
        raise ValueError(f"Day {day} is out of range for month {month} in year {year}")

def sort_dates_by_chronological_order(dates):
    validated_dates = []
    for d in dates:
        validate_date_tuple(d)
        validated_dates.append(d)
    return sorted(validated_dates)

if __name__ == '__main__':
    raw_dates = [
        (2024, 2, 29),
        (2023, 11, 5),
        (2023, 2, 28),
        (2024, 1, 1),
        (2020, 2, 29)
    ]
    sorted_list = sort_dates_by_chronological_order(raw_dates)
    print(sorted_list)