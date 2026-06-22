from datetime import date

def compute_year_difference(date1_str: str, date2_str: str) -> int:
    parts1 = date1_str.split('-')
    parts2 = date2_str.split('-')
    year1 = int(parts1[0])
    year2 = int(parts2[0])
    return abs(year1 - year2)

if __name__ == '__main__':
    start_date = "1995-06-15"
    end_date = "2025-01-01"
    diff = compute_year_difference(start_date, end_date)
    print(diff)