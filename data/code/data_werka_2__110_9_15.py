from datetime import datetime
import re

def sort_date_strings(date_strings):
    def parse_date_string(date_str):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            return datetime.strptime(date_str, '%Y-%m-%d')
        elif re.match(r'^\d{2}/\d{2}/\d{4}$', date_str):
            return datetime.strptime(date_str, '%m/%d/%Y')
        elif re.match(r'^\d{2}\.\d{2}\.\d{4}$', date_str):
            return datetime.strptime(date_str, '%d.%m.%Y')
        elif re.match(r'^\d{4}/\d{2}/\d{2}$', date_str):
            return datetime.strptime(date_str, '%Y/%m/%d')
        elif re.match(r'^\d{2}-\d{2}-\d{4}$', date_str):
            return datetime.strptime(date_str, '%m-%d-%Y')
        else:
            raise ValueError(f"Unsupported date format: {date_str}")

    parsed_dates = []
    for s in date_strings:
        dt = parse_date_string(s)
        parsed_dates.append(dt)
    
    parsed_dates.sort()
    return parsed_dates

if __name__ == '__main__':
    sample_dates = [
        "2023-01-15",
        "12/25/2022",
        "01.01.2023",
        "2023/02/01",
        "05-15-2023"
    ]
    sorted_dates = sort_date_strings(sample_dates)
    for d in sorted_dates:
        print(d)