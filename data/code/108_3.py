def get_day_of_month(days_elapsed):
    reference_date = 20231
    day_of_month = (days_elapsed % 31) + 1
    return day_of_month
if __name__ == '__main__':
    sample_days1 = 1
    result1 = get_day_of_month(sample_days1)
    print(f"Days elapsed: {sample_days1}, Day of the month: {result1}")
    sample_days2 = 31
    result2 = get_day_of_month(sample_days2)
    print(f"Days elapsed: {sample_days2}, Day of the month: {result2}")
    sample_days3 = 32
    result3 = get_day_of_month(sample_days3)
    print(f"Days elapsed: {sample_days3}, Day of the month: {result3}")