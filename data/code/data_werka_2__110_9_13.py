import datetime
import re

def sort_date_strings(date_strings):
    patterns = [
        (r'^\d{4}-\d{2}-\d{2}$', '%Y-%m-%d'),
        (r'^\d{2}/\d{2}/\d{4}$', '%m/%d/%Y'),
        (r'^\d{2}-\d{2}-\d{4}$', '%d-%m-%Y'),
        (r'^\d{4}/\d{2}/\d{2}$', '%Y/%m/%d'),
        (r'^\d{2}\.\d{2}\.\d{4}$', '%d.%m.%Y'),
    ]
    
    parsed_dates = []
    for s in date_strings:
        matched = False
        for pattern, fmt in patterns:
            if re.match(pattern, s):
                try:
                    dt = datetime.datetime.strptime(s, fmt)
                    parsed_dates.append(dt)
                    matched = True
                    break
                except ValueError:
                    continue
        if not matched:
            raise ValueError(f"Unsupported date format: {s}")
            
    sorted_dates = sorted(parsed_dates)
    return sorted_dates

if __name__ == '__main__':
    dates = [
        "2023-01-15",
        "12/25/2022",
        "01-01-2023",
        "2023/02/28",
        "31.12.2022"
    ]
    result = sort_date_strings(dates)
    print(result)