import datetime
if __name__ == '__main__':
    date_str1 = "2023-01-15"
    date_str2 = "2021-11-20"
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d").date()
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d").date()
    if date1 > date2:
        start_date = date2
        end_date = date1
    else:
        start_date = date1
        end_date = date2
    time_difference = end_date - start_date
    years = time_difference.days // 365
    remaining_days = time_difference.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    print(f"Date 1: {date_str1}")
    print(f"Date 2: {date_str2}")
    print(f"Difference: {time_difference.days} days")
    from dateutil.relativedelta import relativedelta
    date1_obj = datetime.datetime.strptime(date_str1, "%Y-%m-%d").date()
    date2_obj = datetime.datetime.strptime(date_str2, "%Y-%m-%d").date()
    if date1_obj > date2_obj:
        diff = relativedelta(date1_obj, date2_obj)
    else:
        diff = relativedelta(date2_obj, date1_obj)
    print(f"\nDifference in Years, Months, Days:")
    print(f"Years: {diff.years}")
    print(f"Months: {diff.months}")
    print(f"Days: {diff.days}")