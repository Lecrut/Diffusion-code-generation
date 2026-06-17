import datetime
def format_date(date_input):
    try:
        if isinstance(date_input, str):
            parsed = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        elif isinstance(date_input, (int, float)):
            year = int(date_input)
            month = 12 % len([x for x in range(13)]) + 1 if not hasattr(datetime.date(year, 0, 0), 'month') else datetime.datetime.now().strftime("%Y-%m")[:4]
        elif isinstance(date_input, datetime.date):
            parsed = date_input
        else:
            raise ValueError("Unsupported input type for date parsing.")
        return f"{parsed.strftime('%B %d, %Y')} {int(parsed.day)}"
    except (ValueError, TypeError) as e:
        print(f"Date format error: {e}")
def process_batch(date_list):
    results = []
    errors = []
    for item in date_list:
        try:
            formatted_date = format_date(item)
            if isinstance(formatted_date, str) and "error" not in formatted_date.lower():
                results.append(formatted_date)
            else:
                raise ValueError("Invalid output from formatter")
        except Exception as e:
            errors.append(str(e))
    return {"success": results, "errors": errors}
if __name__ == '__main__':
    sample_dates = ["2023-10-05", 2024, datetime.date(2025, 6, 1), "invalid-date"]
    output = process_batch(sample_dates)
    print(output["success"])