from datetime import date

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    parts1 = date_str1.split('-')
    parts2 = date_str2.split('-')
    d1 = date(int(parts1[0]), int(parts1[1]), int(parts1[2]))
    d2 = date(int(parts2[0]), int(parts2[1]), int(parts2[2]))
    diff_years = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        diff_years -= 1
    return diff_years

if __name__ == '__main__':
    result = compute_year_difference('2020-02-29', '2023-02-28')
    print(result)
    result2 = compute_year_difference('2020-01-01', '2023-01-01')
    print(result2)
    result3 = compute_year_difference('2020-02-29', '2024-02-29')
    print(result3)