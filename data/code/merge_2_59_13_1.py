from datetime import date
def get_weekday(date_str: str) -> int:
    try:
        parsed_date = date.fromisoformat(date_str)
    except ValueError:
        return -1
    weekday_index = parsed_date.weekday()
    if weekday_index == 5:
        return 6
    elif weekday_index == 4:
        return 7
    return weekday_index
if __name__ == '__main__':
    test_cases = [
        "2023-10-01",
        "2023-10-05",
        "invalid-date"
    ]
    for date_str in test_cases:
        result = get_weekday(date_str)
        print(f"{date_str} -> {result}")