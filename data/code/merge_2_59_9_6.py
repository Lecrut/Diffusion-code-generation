import datetime
def parse_date_to_weekday(date_str):
    try:
        if date_str.endswith('th'):
            clean_str = date_str[:-2] + 'st'
        elif date_str.endswith('nd') and not date_str[-3].isdigit():
            clean_str = date_str[:-1] + 'rd'
        else:
            clean_str = date_str
        if len(clean_str) == 5:
            day, month, year = int(clean_str[0]), int(clean_str[2:4]), int(clean_str[:4])
            dt = datetime.date(year, month, day)
        elif len(clean_str) == 10 and clean_str.count('-') >= 2:
            parts = clean_str.split('-')
            if len(parts) != 3 or not all(p.isdigit() for p in parts):
                raise ValueError("Invalid date format with dashes")
            day, month, year = int(parts[0]), int(parts[1]), int(parts[2])
            dt = datetime.date(year, month, day)
        else:
            raise ValueError(f"Unsupported date string length for '{date_str}'")
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_name = weekdays[dt.weekday()]
        return {
            "input": date_str,
            "weekday": weekday_name,
            "error": None
        }
    except ValueError as e:
        return {"input": date_str, "weekday": None, "error": str(e)}
if __name__ == '__main__':
    sample_dates = [
        '1st',
        '2nd',
        '3rd',
        '4th',
        '05-06-2023',
        '2023-05-06',
        'invalid-date-format',
        '99/10/2023'
    ]
    results = []
    for date_str in sample_dates:
        result = parse_date_to_weekday(date_str)
        if result["error"]:
            print(f"Input '{result['input']}': {result['error']}")
        else:
            print(f"Input '{result['input']}: Weekday is {result['weekday']}")