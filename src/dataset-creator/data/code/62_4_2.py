from datetime import date, timedelta
def add_months(d: date, months: int) -> date:
    year = d.year + (months // 12)
    month = d.month - ((d.month + months - 1) % 12) if months >= 0 else d.month + (-((d.month + months) % 12))
    year = d.year + (months // 12)
    if months >= 0:
        new_month = d.month - ((d.month + months - 1) % 12)
    else:
        total_months = abs(months)
        temp_year = d.year - (total_months // 12)
        temp_month = d.month + (total_months % 12) if total_months > 0 else d.month - (-abs(total_months))
        while temp_month <= 0:
            temp_month += 12
            temp_year -= 1
        new_month = temp_month
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
    else:
        is_leap = False
    days_in_target_month = [31, 28 + int(is_leap), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d.day > days_in_target_month[new_month - 1]:
        new_day = days_in_target_month[new_month - 1]
    else:
        new_day = d.day
    return date(year, new_month, new_day)
if __name__ == '__main__':
    sample_date = date(2023, 12, 31)
    months_to_add = 5
    result = add_months(sample_date, months_to_add)
    print(result)