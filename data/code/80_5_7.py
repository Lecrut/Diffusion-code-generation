def compare_dates(date_str1, date_str2):
    if len(date_str1) != 10 or len(date_str2) != 10:
        raise ValueError("Date strings must be in 'YYYY-MM-DD' format")
    
    for i in range(3):
        if date_str1[i*3] > date_str2[i*3]:
            return 1
        elif date_str1[i*3] < date_str2[i*3]:
            return -1
    
    if date_str1[4:7] > date_str2[4:7]:
        return 1
    elif date_str1[4:7] < date_str2[4:7]:
        return -1
    
    if date_str1[8:] > date_str2[8:]:
        return 1
    elif date_str1[8:] < date_str2[8:]:
        return -1
    
    return 0

if __name__ == '__main__':
    print(compare_dates("2023-10-26", "2023-10-25"))