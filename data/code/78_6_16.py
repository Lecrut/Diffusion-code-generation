import calendar

def months_difference(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    if day1 > day2:
        _, last_day = calendar.monthrange(year2, month2)
        day2 += last_day - day1 + 1
    return (year2 - year1) * 12 + month2 - month1
if __name__ == '__main__':
    date_str1 = '2023-04-15'
    date_str2 = '2022-08-20'
    print(months_difference(date_str1, date_str2))