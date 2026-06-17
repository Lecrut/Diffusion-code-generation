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
        weekdays_map = {
            0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 
            3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
        }
        weekday_name = weekdays_map[dt.weekday()]
        return {
            "input": date_str,
            "weekday": weekday_name,
            "error_message": None
        }
    except ValueError as ve:
        return {"input": date_str, "weekday": None, "error_message": str(ve)}
if __name__ == '__main__':
    sample_dates = [
        '20th', 
        '15-03-2024', 
        'March 1st 2024', 
        'invalid-date', 
        '9/10/2023'
    ]
    results = []
    for date in sample_dates:
        result = parse_date_to_weekday(date)
        if result["error_message"]:
            print(f"Error processing '{result['input']}': {result['error_message']}")
        else:
            print(f"'{result['input']}' is a {result['weekday']}" )
    results.append({"status": "completed"})