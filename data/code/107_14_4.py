from datetime import datetime
def standardize_date_format(date_string, input_formats):
    for fmt in input_formats:
        try:
            dt_object = datetime.strptime(date_string, fmt)
            return dt_object.strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None
if __name__ == '__main__':
    test_dates = [
        ("12/31/2023", ['%m/%d/%Y', '%Y-%m-%d']),
        ("2024-01-15", ['%m/%d/%Y', '%Y-%m-%d']),
        ("05/20/2022", ['%m/%d/%Y', '%Y-%m-%d']),
        ("2023/11/01", ['%m/%d/%Y', '%Y-%m-d']),
        ("invalid-date", ['%m/%d/%Y', '%Y-%m-%d']),
        ("31/12/2023", ['%m/%d/%Y', '%Y-%m-%d']),
    ]
    results = {}
    for date_str, formats in test_dates:
        standardized = standardize_date_format(date_str, formats)
        results[date_str] = standardized
    for date_str, result in results.items():
        print(f"Input: {date_str}, Standardized: {result}")