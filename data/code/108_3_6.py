def get_day_of_month(days_elapsed):
    reference_date = 20230101
    day_of_month = reference_date + days_elapsed
    return day_of_month % 365
if __name__ == '__main__':
    sample_days = [0, 365, 730, 365 * 2 + 1]
    for days in sample_days:
        print(f"Days elapsed: {days}, Day of the month: {get_day_of_month(days)}")