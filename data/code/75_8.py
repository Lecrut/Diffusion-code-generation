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
    print(f"Start Date: {start_date.strftime('%Y-%m-%d')}")
    print(f"End Date: {end_date.strftime('%Y-%m-%d')}")
    print("Difference:")
    total_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    years_final = end_date.year - start_date.year
    months_final = end_date.month - start_date.month
    if months_final < 0:
        years_final -= 1
        months_final += 12
    if years_final > 0:
        months_final %= 12
    if months_final < 0:
        years_final -= 1
        months_final += 12
    days_final = end_date.day - start_date.day
    if days_final < 0:
        months_final -= 1
        days_final += 30
    if days_final < 0:
        years_final -= 1
        months_final += 12
        days_final += 30
    print(f"Difference: {years_final} years, {months_final} months, and {days_final} days")