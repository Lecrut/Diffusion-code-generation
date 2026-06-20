from datetime import date

def are_dates_identical(date_str1: str, date_str2: str) -> bool:
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)
if __name__ == '__main__':
    print(are_dates_identical('2023-04-01', '2023-04-01'))
    print(are_dates_identical('2023-04-01', '2023-04-02'))