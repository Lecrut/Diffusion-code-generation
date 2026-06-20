import calendar

def months_difference(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    year_diff = year2 - year1
    month_diff = month2 - month1
    if year_diff == 0 and month_diff < 0 or year_diff < 0:
        return -1
    total_months_difference = year_diff * 12 + month_diff
    return total_months_difference
if __name__ == '__main__':
    date1 = '2023-04-15'
    date2 = '2022-07-20'
    print(months_difference(date1, date2))