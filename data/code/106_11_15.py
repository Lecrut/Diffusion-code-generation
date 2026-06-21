from datetime import datetime

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    dt1 = datetime.strptime(date_str1, '%Y-%m-%d')
    dt2 = datetime.strptime(date_str2, '%Y-%m-%d')
    return abs(dt1.year - dt2.year)

if __name__ == '__main__':
    result = compute_year_difference('2020-01-01', '2023-12-31')
    print(result)