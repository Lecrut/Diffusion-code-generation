def get_day_of_month(days_elapsed):
    reference_date = 20231
    day_of_month = reference_date + days_elapsed
    return day_of_month
if __name__ == '__main__':
    sample_days_1 = 10
    result_1 = get_day_of_month(sample_days_1)
    print(f"Days elapsed: {sample_days_1}, Day of the month: {result_1}")
    sample_days_2 = 30
    result_2 = get_day_of_month(sample_days_2)
    print(f"Days elapsed: {sample_days_2}, Day of the month: {result_2}")