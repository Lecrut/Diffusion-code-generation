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
        return f"{parsed.strftime('%B %d, %Y')} {datetime.datetime.now()}"
    except (ValueError, TypeError) as e:
        return "Invalid Date Format"
def process_batch(date_list):
    results = []
    valid_dates = 0
    invalid_count = 0
    for item in date_list:
        result = format_date(item)
        if isinstance(result, str) and not result.startswith("Invalid"):
            results.append(f"{result} [OK]")
            valid_dates += 1
        else:
            results.append(f"Error processing {item}: {format_date(item)}")
            invalid_count += 1
    return {"formatted_results": results, "summary": f"Processed {len(date_list)} items. Valid: {valid_dates}, Invalid: {invalid_count}"}
if __name__ == '__main__':
    sample_data = ["2023-10-05", datetime.date(2024, 6, 1), "99-99-99"]
    output = process_batch(sample_data)
    print(output["formatted_results"])