import datetime
def parse_date(date_string: str) -> datetime.date | None:
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None
if __name__ == '__main__':
    start_date_str = "2023-10-05"
    end_date_str = "2024-01-15"
    date_1 = parse_date(start_date_str)
    date_2 = parse_date(end_date_str)
    if not (date_1 and date_2):
        print("Error: Invalid date format provided.")
        exit(1)
    delta_days = abs((date_2 - date_1).days)
    print(f"Days between {start_date_str} and {end_date_str}: {delta_days}")