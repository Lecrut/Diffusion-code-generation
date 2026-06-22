import re

def get_day_from_date(date_str):
    pattern = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
    validation_result = pattern.match(date_str)
    if validation_result is None:
        raise ValueError("Format must be YYYY-MM-DD")
    day_part = validation_result.group(3)
    return day_part

if __name__ == '__main__':
    current_date = "2024-07-19"
    extracted_day = get_day_from_date(current_date)
    print(extracted_day)