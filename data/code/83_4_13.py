from datetime import date

def validate_date_format(date_str: str) -> bool:
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    if not (validate_date_format(date_str1) and validate_date_format(date_str2)):
        raise ValueError("Both inputs must be in 'YYYY-MM-DD' format.")
    
    return date.fromisoformat(date_str1) == date.fromisoformat(date_str2)

if __name__ == '__main__':
    print(dates_are_identical('2023-04-01', '2023-04-01'))
    print(dates_are_identical('2023-04-01', '2023-04-02'))