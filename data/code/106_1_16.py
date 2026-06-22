from datetime import date

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    try:
        parts1 = date_str1.split('-')
        parts2 = date_str2.split('-')
        if len(parts1) != 3 or len(parts2) != 3:
            raise ValueError('Invalid date format')
        year1 = int(parts1[0])
        month1 = int(parts1[1])
        day1 = int(parts1[2])
        year2 = int(parts2[0])
        month2 = int(parts2[1])
        day2 = int(parts2[2])
        date1 = date(year1, month1, day1)
        date2 = date(year2, month2, day2)
        diff_years = date2.year - date1.year
        if (date2.month, date2.day) < (date1.month, date1.day):
            diff_years -= 1
        return diff_years
    except (ValueError, IndexError) as e:
        raise ValueError(f'Invalid date input: {e}')
if __name__ == '__main__':
    result = compute_year_difference('2020-02-29', '2023-03-01')
    print(result)
    result2 = compute_year_difference('2020-02-29', '2023-02-28')
    print(result2)
    result3 = compute_year_difference('2020-01-01', '2020-12-31')
    print(result3)