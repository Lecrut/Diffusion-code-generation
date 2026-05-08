from datetime import datetime
def parse_and_standardize_dates(date_strings, formats):
    standardized_dates = {}
    for i, date_str in enumerate(date_strings):
        parsed_date = None
        for fmt in formats:
            try:
                parsed_date = datetime.strptime(date_str, fmt)
                standardized_dates[f"date_{i}"] = parsed_date
                break
            except ValueError:
                continue
        if parsed_date is None:
            standardized_dates[f"date_{i}"] = None
    return standardized_dates
if __name__ == '__main__':
    date_inputs = [
        "2023-01-15",
        "02/28/2023",
        "15-Feb-2023",
        "2023/03/01"
    ]
    date_formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%b-%Y",
        "%Y/%m/%d"
    ]
    results = parse_and_standardize_dates(date_inputs, date_formats)
    for key, value in results.items():
        print(f"{key}: {value}")