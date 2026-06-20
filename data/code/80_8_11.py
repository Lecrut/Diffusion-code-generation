from datetime import date

def parse_date(date_str: str) -> date:
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise ValueError('Invalid date format. Please use ISO 8601 format (YYYY-MM-DD).')

def compare_dates(date1: date, date2: date) -> int:
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0

def format_date(date_obj: date, format_str: str='%Y-%m-%d') -> str:
    try:
        return date_obj.strftime(format_str)
    except ValueError:
        raise ValueError('Invalid format string. Please use a valid strftime format.')
if __name__ == '__main__':
    sample_date1 = parse_date('2023-10-26')
    sample_date2 = parse_date('2024-01-01')
    print(f'Comparison result: {compare_dates(sample_date1, sample_date2)}')
    print(f'Formatted date: {format_date(sample_date1, '%d/%m/%Y')}')