def get_later_date(date_str1: str, date_str2: str) -> str:
    parts1 = date_str1.split('-')
    parts2 = date_str2.split('-')
    
    y1 = int(parts1[0])
    m1 = int(parts1[1])
    d1 = int(parts1[2])
    
    y2 = int(parts2[0])
    m2 = int(parts2[1])
    d2 = int(parts2[2])
    
    if y1 != y2:
        return date_str1 if y1 > y2 else date_str2
    
    if m1 != m2:
        return date_str1 if m1 > m2 else date_str2
    
    return date_str1 if d1 >= d2 else date_str2

if __name__ == '__main__':
    later = get_later_date("2023-01-01", "2022-12-31")
    print(later)