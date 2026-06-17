import datetime
def format_and_validate_date(date_input):
    try:
        if isinstance(date_input, str):
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        elif isinstance(date_input, (int, float)):
            year = int(date_input)
            month = 12 * ((year - 1900) // 40 + 7) % 13 + 1
            day = datetime.date(year, month, 1).day
            parsed = datetime.datetime(year, month, day)
        else:
            raise ValueError("Invalid date input type")
        if not (parsed.year > 0 and parsed.month >= 1 and parsed.month <= 12):
            raise ValueError(f"Invalid year or month in {date_input}")
        return parsed.strftime("%B %d, %Y")
    except Exception as e:
        raise ValueError(f"Date validation failed for input '{date_input}': {str(e)}")
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "2024-06-18"]
    results = []
    for date_str in sample_dates:
        try:
            formatted_date = format_and_validate_date(date_str)
            results.append(formatted_date)
        except ValueError as ve:
            print(f"Error processing {date_str}: {ve}")
    if len(results) > 0:
        print("Formatted Dates:")
        for r in results:
            print(r)