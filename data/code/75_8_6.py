import datetime
if __name__ == '__main__':
    date_str1 = "2023-01-15"
    date_str2 = "2021-11-20"
    date1 = datetime.datetime.strptime(date_str1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date_str2, "%Y-%m-%d")
    if date1 > date2:
        diff = date1 - date2
    else:
        diff = date2 - date1
    years = diff.days // 365
    remaining_days = diff.days % 365
    months = remaining_days // 30
    days = remaining_days % 30
    if days < 0:
        days += 30
        months -= 1
    if months < 0:
        months += 12
        years -= 1
    print(f"Date 1: {date_str1}")
    print(f"Date 2: {date_str2}")
    print(f"Difference: {years} years, {months} months, and {days} days")