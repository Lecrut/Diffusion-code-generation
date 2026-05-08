def get_day_of_month(days_elapsed):
    reference_date = 20230101
    day_of_year = reference_date + days_elapsed
    return day_of_year % 365
if __name__ == '__main__':
    sample_days = [0, 1, 365, 366, 730]
    for days in sample_days:
        print(f"Days elapsed: {days}, Day of the month: {get_day_of_month(days)}")