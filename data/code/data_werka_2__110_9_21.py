import datetime
import re

def sort_date_strings(date_strings):
    patterns = [
        (r'(\d{4})[-/](\d{1,2})[-/](\d{1,2})', '%Y-%m-%d'),
        (r'(\d{1,2})[-/](\d{1,2})[-/](\d{4})', '%m-%d-%Y'),
        (r'(\d{1,2})[-/](\d{1,2})[-/](\d{2})', '%m-%d-%y'),
    ]
    
    parsed_dates = []
    for ds in date_strings:
        matched = False
        for pattern, fmt in patterns:
            if re.match(pattern, ds):
                try:
                    dt = datetime.datetime.strptime(ds, fmt)
                    parsed_dates.append(dt)
                    matched = True
                    break
                except ValueError:
                    continue
        if not matched:
            raise ValueError(f"Unsupported date format: {ds}")
    
    sorted_dates = sorted(parsed_dates)
    return [dt.strftime('%Y-%m-%d') for dt in sorted_dates]

if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "15/01/2023",
        "01-15-2023",
        "2022-12-31",
        "31/12/2022",
        "12-31-2022",
        "2023-02-01",
        "01/02/2023",
        "02-01-2023"
    ]
    result = sort_date_strings(sample_dates)
    print(result)