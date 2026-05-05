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
    if months >= 12:
        years += months // 12
        days = (remaining_days % 12) * 30 + days
        months = (remaining_days // 12) % 12
    else:
        days = remaining_days
        months = remaining_days // 30
        days = remaining_days % 30
    print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
    print(f"End Date: {end_date.strftime('%Y-%m-%d')}")
    print(f"Difference: {years} years, {months} months, and {days} days")