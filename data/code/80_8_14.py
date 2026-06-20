from datetime import date

def parse_date(date_str: str) -> date:
    try:
        return date.fromisoformat(date_str)
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD, got {date_str}") from e

def compare_dates(date1: date, date2: date) -> int:
    if date1 == date2:
        return 0
    elif date1 < date2:
        return -1
    else:
        return 1

def format_date(date_obj: date, format_str: str = "%Y-%m-%d") -> str:
    try:
        return date_obj.strftime(format_str)
    except ValueError as e:
        raise ValueError(f"Invalid format string. Got {format_str}") from e

if __name__ == '__main__':
    date1_str = "2023-10-26"
    date2_str = "2023-01-01"

    parsed_date1 = parse_date(date1_str)
    parsed_date2 = parse_date(date2_str)

    comparison_result = compare_dates(parsed_date1, parsed_date2)
    print(f"Comparison Result: {comparison_result}")

    formatted_date1 = format_date(parsed_date1)
    print(f"Formatted Date 1: {formatted_date1}")