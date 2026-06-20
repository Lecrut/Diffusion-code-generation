import re

def extract_day(date_str):
    match = re.search(r'\d{4}-\d{2}-(\d{2})', date_str)
    if match:
        return match.group(1)

if __name__ == '__main__':
    sample_date = '2023-09-15'
    print(extract_day(sample_date))