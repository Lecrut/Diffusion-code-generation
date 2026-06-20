import calendar

def months_between_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    year_diff = year2 - year1
    month_diff = month2 - month1
    if day2 < day1:
        month_diff -= 1
        _, last_day_of_prev_month = calendar.monthrange(year2, month2)
        day2 += last_day_of_prev_month
    total_months_diff = year_diff * 12 + month_diff
    return total_months_diff
if __name__ == '__main__':
    date1 = '2020-01-15'
    date2 = '2023-04-10'
    print(months_between_dates(date1, date2))