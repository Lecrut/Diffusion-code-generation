def compare_dates(date_str1, date_str2):
    if len(date_str1) != 10 or len(date_str2) != 10:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    for i in [4, 7]:
        if date_str1[i] != '-' or date_str2[i] != '-':
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    year1 = int(date_str1[:4])
    month1 = int(date_str1[5:7])
    day1 = int(date_str1[8:])
    
    year2 = int(date_str2[:4])
    month2 = int(date_str2[5:7])
    day2 = int(date_str2[8:])
    
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
    result = compare_dates("2023-10-26", "2023-10-25")
    print(result)