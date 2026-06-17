import datetime
def parse_date(date_string: str) -> datetime.date | None:
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None
if __name__ == '__main__':
    date1_str = "2023-10-05"
    date2_str = "2024-01-15"
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)
    if not (date1 and date2):
        print("Invalid date format provided.")
        exit(1)
    delta = abs((date2 - date1).days)
    print(f"Days between {date1} and {date2}: {delta}")