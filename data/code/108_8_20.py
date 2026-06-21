from dateutil.parser import parse

DAY_MAPPING = {
    "iso": "%Y-%m-%d",
    "us": "%B %d, %Y",
    "eu": "%d.%m.%Y"
}

def extract_day(date_string: str) -> int:
    parsed_date = parse(date_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_dates = {
        "iso": "2023-10-25",
        "us": "July 4, 1776",
        "eu": "25.12.2023"
    }
    for key, date_str in sample_dates.items():
        day_number = extract_day(date_str)
        print(day_number)