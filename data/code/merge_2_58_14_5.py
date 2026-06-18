import datetime
def parse_date(date_str: str) -> datetime.date | None:
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
if __name__ == '__main__':
    start_date = "2023-10-05"
    end_date = "2024-01-15"
    parsed_start = parse_date(start_date)
    parsed_end = parse_date(end_date)
    if not (parsed_start and parsed_end):
        print("Invalid date format provided.")
        exit(1)
    delta_days = abs((parsed_end - parsed_start).days)
    print(f"Days between {start_date} and {end_date}: {delta_days}")