from datetime import date

def parse_date(date_str: str) -> date:
    try:
        return date.fromisoformat(date_str)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e

def dates_are_identical(date_str1: str, date_str2: str) -> bool:
    parsed_date1 = parse_date(date_str1)
    parsed_date2 = parse_date(date_str2)
    return parsed_date1 == parsed_date2

if __name__ == '__main__':
    print(dates_are_identical('2023-04-01', '2023-04-01'))
    print(dates_are_identical('2023-04-01', '2023-04-02'))