from datetime import date

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    try:
        return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)
    except ValueError:
        raise ValueError("Input strings must be in 'YYYY-MM-DD' format.")

if __name__ == '__main__':
    print(dates_are_identical('2023-04-01', '2023-04-01'))
    print(dates_are_identical('2023-04-01', '2023-04-02'))