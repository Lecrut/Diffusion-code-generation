import re
from datetime import datetime

def sort_date_strings(date_strings):
    def parse_date(date_str):
        patterns = [
            ("%Y-%m-%d", re.compile(r"^\d{4}-\d{2}-\d{2}$")),
            ("%d/%m/%Y", re.compile(r"^\d{2}/\d{2}/\d{4}$")),
            ("%m-%d-%Y", re.compile(r"^\d{2}-\d{2}-\d{4}$")),
            ("%Y/%m/%d", re.compile(r"^\d{4}/\d{2}/\d{2}$")),
            ("%d.%m.%Y", re.compile(r"^\d{2}\.\d{2}\.\d{4}$")),
            ("%Y.%m.%d", re.compile(r"^\d{4}\.\d{2}\.\d{2}$")),
            ("%m/%d/%Y", re.compile(r"^\d{2}/\d{2}/\d{4}$")),
            ("%d-%m-%Y", re.compile(r"^\d{2}-\d{2}-\d{4}$")),
        ]
        
        for fmt, regex in patterns:
            if regex.match(date_str):
                try:
                    return datetime.strptime(date_str, fmt)
                except ValueError:
                    continue
        
        raise ValueError(f"Unsupported date format: {date_str}")

    parsed_dates = []
    for date_str in date_strings:
        dt = parse_date(date_str)
        parsed_dates.append((dt, date_str))
    
    parsed_dates.sort(key=lambda x: x[0])
    
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "15/01/2023",
        "01-15-2023",
        "2023/01/15",
        "15.01.2023",
        "2023.01.15",
        "01/15/2023",
        "15-01-2023"
    ]
    
    result = sort_date_strings(sample_dates)
    print(result)