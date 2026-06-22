import datetime
import re

def sort_date_strings(date_strings):
    patterns = [
        (r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', '%Y-%m-%d'),
        (r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', '%m-%d-%Y'),
        (r'(\d{1,2})[-/](\d{1,2})[-/](\d{2})', '%m-%d-%y'),
    ]
    
    def parse_date(s):
        s = s.strip()
        for pattern, fmt in patterns:
            if re.match(pattern, s):
                try:
                    return datetime.datetime.strptime(s, fmt)
                except ValueError:
                    continue
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
        "01/15/2023",
        "15-01-2023",
        "2023-12-31",
        "31/12/2023",
        "2023-06-15",
        "15/06/2023",
        "2023-02-28",
        "28-02-2023",
        "2023-03-01"
    ]
    
    sorted_dates = sort_date_strings(sample_dates)
    print(sorted_dates)