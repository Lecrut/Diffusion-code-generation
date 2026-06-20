import re

def extract_day(date_str):
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        return int(match.group(3))
    else:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    sample_date1 = "2023-04-15"
    day1 = extract_day(sample_date1)
    print(f"Date: {sample_date1}, Day: {day1}")

    sample_date2 = "2023-12-25"
    day2 = extract_day(sample_date2)
    print(f"Date: {sample_date2}, Day: {day2}")