from datetime import date

def parse_date(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date string must be in 'YYYY-MM-DD' format.")
    return date(int(parts[0]), int(parts[1]), int(parts[2]))

def compare_dates(date_str, date_obj):
    parsed_date = parse_date(date_str)
    return min(parsed_date, date_obj)

if __name__ == '__main__':
    result = compare_dates('2023-04-01', date(2023, 5, 1))
    print(result)