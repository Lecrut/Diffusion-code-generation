from datetime import date

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    parts1 = date_str1.split('-')
    parts2 = date_str2.split('-')
    
    y1, m1, d1 = int(parts1[0]), int(parts1[1]), int(parts1[2])
    y2, m2, d2 = int(parts2[0]), int(parts2[1]), int(parts2[2])
    
    try:
        dt1 = date(y1, m1, d1)
        dt2 = date(y2, m2, d2)
    except ValueError:
        raise ValueError("Invalid date format or values")
    
    diff = dt2 - dt1
    years = diff.days // 365
    
    if diff.days < 0:
        years = -(-diff.days // 365)
        
    return years

if __name__ == '__main__':
    result = compute_year_difference("2020-01-01", "2023-01-01")
    print(result)