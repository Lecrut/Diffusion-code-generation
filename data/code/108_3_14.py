from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def extract_day(date_str: str) -> int:
    parsed_date = datetime.strptime(date_str, DATE_FORMAT)
    return parsed_date.day

if __name__ == '__main__':
    sample_date = "2023-10-05"
    day_value = extract_day(sample_date)
    print(day_value)