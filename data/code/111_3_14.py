from datetime import date

def subtract_months_from_date(target_date, months_to_subtract):
    total_months = target_date.year * 12 + target_date.month
    adjusted_total = total_months - months_to_subtract
    new_year = adjusted_total // 12
    new_month = adjusted_total % 12
    if new_month == 0:
        new_month = 12
        new_year -= 1
    if new_year < 1:
        raise ValueError("Resulting date is before year 1")
    last_day_of_month = 28
    for day in range(28, 32):
        try:
            date(new_year, new_month, day)
            last_day_of_month = day
        except ValueError:
            break
    if target_date.day > last_day_of_month:
        new_day = last_day_of_month
    else:
        new_day = target_date.day
    return date(new_year, new_month, new_day)

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    months_to_sub = 3
    result_date = subtract_months_from_date(sample_date, months_to_sub)
    print(result_date)