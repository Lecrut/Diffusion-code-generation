import datetime
import re

def sort_date_strings(date_strings):
    patterns = [
        (r"(\d{4})[-/](\d{1,2})[-/](\d{1,2})", "%Y-%m-%d"),
        (r"(\d{1,2})[-/](\d{1,2})[-/](\d{4})", "%d-%m-%Y"),
        (r"(\d{1,2})[-/](\d{1,2})[-/](\d{2,4})", "%d-%m-%Y"),
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
    dates = [
        "2023-01-15",
        "15/01/2023",
        "2022-12-31",
        "31-12-2022",
        "2023-02-01"
    ]
    result = sort_date_strings(dates)
    print(result)