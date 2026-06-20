def compare_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))

    if year1 > year2:
        return 1
    elif year1 < year2:
        return -1

    if month1 > month2:
        return 1
    elif month1 < month2:
        return -1

    if day1 > day2:
        return 1
    elif day1 < day2:
        return -1

    return 0

if __name__ == '__main__':
    result = compare_dates('2023-11-05', '2023-11-04')
    print(result)