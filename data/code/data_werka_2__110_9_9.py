import datetime
import re

def sort_date_strings(date_strings):
    patterns = [
        (r'^\d{4}-\d{2}-\d{2}$', '%Y-%m-%d'),
        (r'^\d{2}/\d{2}/\d{4}$', '%m/%d/%Y'),
        (r'^\d{2}-\d{2}-\d{4}$', '%m-%d-%Y'),
        (r'^\d{4}\.\d{2}\.\d{2}$', '%Y.%m.%d'),
        (r'^\d{2}\.\d{2}\.\d{4}$', '%d.%m.%Y'),
    ]
    
    def parse_date(s):
        for pattern, fmt in patterns:
            if re.match(pattern, s):
                return datetime.datetime.strptime(s, fmt)
        raise ValueError(f"Unsupported date format: {s}")
    
    parsed_dates = []
    for s in date_strings:
        dt = parse_date(s)
        parsed_dates.append((dt, s))
    
    parsed_dates.sort(key=lambda x: x[0])
    
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "12/25/2022",
        "01-01-2023",
        "2023.05.20",
        "25.12.2022",
        "2022-12-31"
    ]
    result = sort_date_strings(sample_dates)
    print(result)