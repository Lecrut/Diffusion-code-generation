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

def format_date(date_obj: date, fmt: str = '%Y-%m-%d') -> str:
    return date_obj.strftime(fmt)

if __name__ == '__main__':
    date_str1 = '2023-10-26'
    date_str2 = '2023-01-01'
    
    parsed_date1 = parse_date(date_str1)
    parsed_date2 = parse_date(date_str2)
    
    comparison_result = compare_dates(parsed_date1, parsed_date2)
    formatted_date = format_date(parsed_date1)
    
    print(f"Parsed Date 1: {parsed_date1}")
    print(f"Parsed Date 2: {parsed_date2}")
    print(f"Comparison Result: {comparison_result}")
    print(f"Formatted Date: {formatted_date}")