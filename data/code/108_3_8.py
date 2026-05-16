def get_day_of_month(days_elapsed):
    reference_date = 20230101
    day_of_month = reference_date + days_elapsed
    return day_of_month % 365
if __name__ == '__main__':
    sample_days_1 = 10
    result_1 = get_day_of_month(sample_days_1)
    print(result_1)
    sample_days_2 = 365
    result_2 = get_day_of_month(sample_days_2)
    print(result_2)
    sample_days_3 = 366
    result_3 = get_day_of_month(sample_days_3)
    print(result_3)