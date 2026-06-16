def compare_dates(date1_str, date2_str):
    parts1 = date1_str.split('-')
    parts2 = date2_str.split('-')
    if len(parts1) != 3 or len(parts2) != 3:
        raise ValueError("Invalid date format")
    year1 = int(parts1[0])
    month1 = int(parts1[1])
    day1 = int(parts1[2])
    year2 = int(parts2[0])
    month2 = int(parts2[1])
    day2 = int(parts2[2])
    if year1 < year2:
        return True
    elif year1 > year2:
        return False
    else:
        if month1 < month2:
            return True
        elif month1 > month2:
            return False
        else:
            if day1 < day2:
                return True
            elif day1 > day2:
                return False
            else:
                return False
if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2024-01-15"
    print(f"{date_a} precedes {date_b}: {compare_dates(date_a, date_b)}")
    date_c = "2025-03-01"
    date_d = "2025-03-01"
    print(f"{date_c} precedes {date_d}: {compare_dates(date_c, date_d)}")
    date_e = "2024-12-31"
    date_f = "2024-12-30"
    print(f"{date_e} precedes {date_f}: {compare_dates(date_e, date_f)}")
    date_g = "2023-11-01"
    date_h = "2023-10-31"
    print(f"{date_g} precedes {date_h}: {compare_dates(date_g, date_h)}")
    date_i = "2024-05-10"
    date_j = "2024-05-10"
    print(f"{date_i} precedes {date_j}: {compare_dates(date_i, date_j)}")