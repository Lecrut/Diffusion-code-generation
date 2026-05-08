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
    dates_to_convert = [
        ('01/15/2023', ['%m/%d/%Y', '%Y-%m-%d']),
        ('2024-05-20', ['%m/%d/%Y', '%Y-%m-%d']),
        ('12/31/2022', ['%m/%d/%Y', '%Y-%m-d']),
        ('2025/01/01', ['%m/%d/%Y', '%Y-%m-%d'])
    ]
    results = {}
    for date_str, formats in dates_to_convert:
        standard_date = standardize_date_format(date_str, formats)
        results[date_str] = standard_date
    print(results)