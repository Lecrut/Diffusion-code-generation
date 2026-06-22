from datetime import datetime

def compute_year_difference(date_str1: str, date_str2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date_str1, fmt)
    d2 = datetime.strptime(date_str2, fmt)
    years = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        years -= 1
    return years

if __name__ == '__main__':
    result = compute_year_difference("2020-02-29", "2023-02-28")
    print(result)