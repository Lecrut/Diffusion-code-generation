def compare_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    
    if year1 > year2:
        return True
    elif year1 < year2:
        return False
    
    if month1 > month2:
        return True
    elif month1 < month2:
        return False
    
    if day1 > day2:
        return True
    else:
        return False

if __name__ == '__main__':
    date_a = "2023-10-25"
    date_b = "2023-10-26"
    result1 = compare_dates(date_a, date_b)
    print(result1)
    
    date_c = "2024-01-01"
    date_d = "2023-12-31"
    result2 = compare_dates(date_c, date_d)
    print(result2)
    
    date_e = "2025-05-05"
    date_f = "2025-04-30"
    result3 = compare_dates(date_e, date_f)
    print(result3)