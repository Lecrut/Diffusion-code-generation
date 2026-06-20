from datetime import date

def parse_date(date_str: str) -> date:
    return date.fromisoformat(date_str)

def compare_dates(date1: date, date2: date) -> int:
    if date1 == date2:
        return 0
    elif date1 < date2:
        return -1
    else:
        return 1

def format_date(date_obj: date, format_str: str = "%Y-%m-%d") -> str:
    return date_obj.strftime(format_str)

if __name__ == '__main__':
    sample_date1 = "2023-10-26"
    parsed_date1 = parse_date(sample_date1)
    print(f"Parsed Date 1: {parsed_date1}")

    sample_date2 = "2024-01-01"
    parsed_date2 = parse_date(sample_date2)
    print(f"Parsed Date 2: {parsed_date2}")

    comparison_result = compare_dates(parsed_date1, parsed_date2)
    print(f"Comparison Result (Date 1 vs Date 2): {comparison_result}")

    formatted_date = format_date(parsed_date1, "%d %B %Y")
    print(f"Formatted Date 1: {formatted_date}")