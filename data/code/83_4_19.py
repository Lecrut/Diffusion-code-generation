from datetime import date

def dates_identical(date_str1: str, date_str2: str) -> bool:
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)
if __name__ == '__main__':
    print(dates_identical('2023-04-01', '2023-04-01'))
    print(dates_identical('2023-04-01', '2023-04-02'))