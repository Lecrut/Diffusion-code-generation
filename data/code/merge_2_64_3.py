import datetime
def format_date(date_str: str) -> str | None:
    try:
        parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return parsed.strftime("%B %d, %Y")
    except ValueError:
        return f"Error: Invalid date format '{date_str}'. Expected YYYY-MM-DD."
def process_batch(input_dates: list[str]) -> list[str]:
    results = []
    for item in input_dates:
        result = format_date(item)
        if isinstance(result, str):
            results.append(f"[{result}]")
    return results
if __name__ == '__main__':
    sample_data = ["2023-10-05", "invalid-date", "2024-01-15"]
    output = process_batch(sample_data)
    print(output)