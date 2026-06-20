def compare_dates(date1, date2):
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))
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
    print(compare_dates('2023-10-05', '2023-09-30'))
    print(compare_dates('2023-08-15', '2023-08-15'))
    print(compare_dates('2022-12-25', '2023-01-01'))