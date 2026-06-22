import re

def extract_day(date_str):
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_str)
    if not match:
        raise ValueError("Invalid date format")
    return match.group(3)

if __name__ == '__main__':
    print(extract_day("2023-10-05"))