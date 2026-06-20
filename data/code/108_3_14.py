import re

def extract_day(date_str):
    match = re.search('\\d{4}-\\d{2}-(\\d{2})', date_str)
    if match:
        return match.group(1)
    else:
        raise ValueError('Invalid date format')
if __name__ == '__main__':
    sample_date = '2023-09-15'
    day = extract_day(sample_date)
    print(day)