import calendar

def months_difference(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    diff_years = year2 - year1
    diff_months = month2 - month1
    if year2 == year1 and month2 < month1 or year2 < year1:
        diff_months -= 12 * diff_years
    return abs(diff_months)
if __name__ == '__main__':
    print(months_difference('2023-04-15', '2022-02-28'))