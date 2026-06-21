from datetime import date

def calculate_years_gap(start: str, end: str) -> int:
    try:
        parts1 = start.split("-")
        parts2 = end.split("-")
        if len(parts1) != 3 or len(parts2) != 3:
            raise ValueError("Bad format")
        y1, m1, d1 = int(parts1[0]), int(parts1[1]), int(parts1[2])
        y2, m2, d2 = int(parts2[0]), int(parts2[1]), int(parts2[2])
        d1_obj = date(y1, m1, d1)
        d2_obj = date(y2, m2, d2)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Date parsing failed: {e}")
    
    diff_years = abs(d2_obj.year - d1_obj.year)
    if diff_years == 0:
        return 0
    
    earlier = d1_obj if d1_obj < d2_obj else d2_obj
    later = d2_obj if d1_obj < d2_obj else d1_obj
    
    anniversary = date(later.year - diff_years, later.month, later.day)
    if later < anniversary:
        return diff_years - 1
    return diff_years

if __name__ == '__main__':
    val = calculate_years_gap("2010-06-15", "2015-06-14")
    print(val)