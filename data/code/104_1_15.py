def compare_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))

    if year1 > year2:
        return date_str1
    elif year1 < year2:
        return date_str2
    else:
        if month1 > month2:
            return date_str1
        elif month1 < month2:
            return date_str2
        else:
            if day1 > day2:
                return date_str1
            else:
                return date_str2

if __name__ == '__main__':
    date1 = "2023-10-26"
    date2 = "2023-10-25"
    result1 = compare_dates(date1, date2)
    print(result1)

    date3 = "2024-01-01"
    date4 = "2024-01-15"
    result2 = compare_dates(date3, date4)
    print(result2)

    date5 = "2022-12-31"
    date6 = "2023-01-01"
    result3 = compare_dates(date5, date6)
    print(result3)