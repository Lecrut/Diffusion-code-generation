def get_day_of_month(days_elapsed):
    reference_date = 20230101
    day_of_year = reference_date + days_elapsed
    return day_of_year % 365
if __name__ == '__main__':
    sample_days1 = 10
    result1 = get_day_of_month(sample_days1)
    print(f"Days elapsed: {sample_days1}, Day of month: {result1}")
    sample_days2 = 365
    result2 = get_day_of_month(sample_days2)
    print(f"Days elapsed: {sample_days2}, Day of month: {result2}")
    sample_days3 = 366
    result3 = get_day_of_month(sample_days3)
    print(f"Days elapsed: {sample_days3}, Day of month: {result3}")