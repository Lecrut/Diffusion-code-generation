def compare_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))

    if year1 > year2:
        return 1
    elif year1 < year2:
        return -1
    else:
        if month1 > month2:
            return 1
        elif month1 < month2:
            return -1
        else:
            if day1 > day2:
                return 1
            elif day1 < day2:
                return -1
            else:
                return 0

if __name__ == '__main__':
    date_str1 = "2023-04-15"
    date_str2 = "2023-04-16"
    result = compare_dates(date_str1, date_str2)
    print(f"{date_str1} is {'after' if result == 1 else 'before' if result == -1 else 'the same as'} {date_str2}")