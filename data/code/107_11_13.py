import re

DATE_PATTERN = r'(\d{1,2})\/(\d{1,2})\/(\d{4})'

def convert_date_format(date_str):
    match = re.match(DATE_PATTERN, date_str)
    if match:
        month, day, year = match.groups()
        return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
    else:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    sample_date = "10/27/2023"
    result = convert_date_format(sample_date)
    print(result)