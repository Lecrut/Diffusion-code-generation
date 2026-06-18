import datetime
def format_date(date_str: str) -> str | None:
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return "Invalid Date Format"
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "invalid-date", "2024-01-15"]
    results = []
    for date in sample_dates:
        formatted_date = format_date(date)
        if isinstance(formatted_date, str):
            results.append(f"Input: {date} -> Output: {formatted_date}")
    print("\n".join(results))