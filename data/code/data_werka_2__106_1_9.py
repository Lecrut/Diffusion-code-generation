from datetime import date

def year_difference(date_str1: str, date_str2: str) -> int:
    d1 = date.fromisoformat(date_str1)
    d2 = date.fromisoformat(date_str2)
    diff_years = d2.year - d1.year
    if (d2.month, d2.day) < (d1.month, d1.day):
        diff_years -= 1
    return abs(diff_years)

if __name__ == '__main__':
    result = year_difference("2020-02-29", "2023-02-28")
    print(result)