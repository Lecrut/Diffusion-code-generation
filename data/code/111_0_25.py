from datetime import date

def compute_year_span_days(year):
    first_day = date(year, 1, 1)
    last_day = date(year, 12, 31)
    time_difference = last_day - first_day
    day_count = time_difference.days
    return day_count

if __name__ == '__main__':
    sample_year = 2023
    days_in_span = compute_year_span_days(sample_year)
    print(days_in_span)