import calendar

def months_difference(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    _, max_day1 = calendar.monthrange(year1, month1)
    _, max_day2 = calendar.monthrange(year2, month2)
    if day1 > max_day1:
        day1 = max_day1
    if day2 > max_day2:
        day2 = max_day2
    diff_years = year2 - year1
    diff_months = month2 - month1
    total_diff_months = diff_years * 12 + diff_months
    return total_diff_months
if __name__ == '__main__':
    date1 = '2023-04-15'
    date2 = '2022-08-20'
    print(months_difference(date1, date2))