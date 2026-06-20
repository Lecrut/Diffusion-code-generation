from datetime import date

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)

if __name__ == '__main__':
    d1 = date(2023, 5, 15)
    d2 = date(2023, 5, 15)
    print(dates_are_identical(str(d1), str(d2)))