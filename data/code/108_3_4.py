def calculate_day_of_month(days_elapsed):
    reference_date = "2023-01-01"
    days_since_reference = int(days_elapsed)
    reference_date_obj = reference_date
    import datetime
    try:
        reference_date_obj = datetime.datetime.strptime(reference_date, "%Y-%m-%d").date()
        target_date = reference_date_obj + datetime.timedelta(days=days_since_reference)
        return target_date.day
    except ValueError:
        return "Invalid input"
if __name__ == '__main__':
    sample_days_1 = 5
    result_1 = calculate_day_of_month(sample_days_1)
    print(f"Days elapsed: {sample_days_1}, Day of the month: {result_1}")
    sample_days_2 = 365
    result_2 = calculate_day_of_month(sample_days_2)
    print(f"Days elapsed: {sample_days_2}, Day of the month: {result_2}")
    sample_days_3 = 1000
    result_3 = calculate_day_of_month(sample_days_3)
    print(f"Days elapsed: {sample_days_3}, Day of the month: {result_3}")