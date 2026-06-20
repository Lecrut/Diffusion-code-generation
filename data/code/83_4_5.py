from datetime import date

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)

if __name__ == '__main__':
    d1 = '2023-05-15'
    d2 = '2023-05-15'
    print(dates_are_identical(d1, d2))