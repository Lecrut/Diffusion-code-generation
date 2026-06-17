import datetime
def parse_date(date_string: str) -> datetime.date | None:
    try:
        return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return None
if __name__ == '__main__':
    sample_date1 = "2023-05-17"
    sample_date2 = "2024-08-29"
    date_obj_1 = parse_date(sample_date1)
    date_obj_2 = parse_date(sample_date2)
    if not (date_obj_1 and date_obj_2):
        print("Error: Invalid date format provided.")
    else:
        delta_days = abs((date_obj_2 - date_obj_1).days)
        print(f"Days between {sample_date1} and {sample_date2}: {delta_days}")