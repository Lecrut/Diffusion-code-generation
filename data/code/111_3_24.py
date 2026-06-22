from datetime import date

def subtract_months(target_date, months_to_subtract):
    total_months = target_date.year * 12 + target_date.month - months_to_subtract
    new_year = total_months // 12
    new_month = total_months % 12
    if new_month == 0:
        new_month = 12
        new_year -= 1
    max_day = 28
    for day_candidate in range(28, 32):
        try:
            date(new_year, new_month, day_candidate)
            max_day = day_candidate
        except ValueError:
            break
    new_day = min(target_date.day, max_day)
    return date(new_year, new_month, new_day)

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    months_offset = 3
    computed_date = subtract_months(sample_date, months_offset)
    print(computed_date)