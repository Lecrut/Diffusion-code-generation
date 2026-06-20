import calendar

def months_between_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    years_diff = year2 - year1
    months_diff = month2 - month1
    if day2 < day1:
        months_diff -= 1
        _, last_day_of_prev_month = calendar.monthrange(year2, month2)
        day2 += last_day_of_prev_month
    total_months_diff = years_diff * 12 + months_diff
    return total_months_diff
if __name__ == '__main__':
    date_str1 = '2022-03-15'
    date_str2 = '2023-07-20'
    print(months_between_dates(date_str1, date_str2))