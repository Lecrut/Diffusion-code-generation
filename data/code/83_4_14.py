from datetime import date

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)

if __name__ == '__main__':
    print(dates_are_identical('2023-12-25', '2023-12-25'))
    print(dates_are_identical('2023-12-26', '2023-12-27'))