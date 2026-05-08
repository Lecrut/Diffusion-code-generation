from datetime import datetime
def standardize_date(date_string, input_formats):
    for fmt in input_formats:
        try:
            dt_object = datetime.strptime(date_string, fmt)
            return dt_object.strftime('%Y-%m-%d')
        except ValueError:
            continue
    return None
if __name__ == '__main__':
    date1 = '12/31/2023'
    date2 = '2024-01-15'
    date3 = '05/20/2022'
    date4 = '2023/11/01'
    invalid_date = '2023-13-01'
    formats_to_try = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d']
    print(f"Input: {date1}, Formats: {formats_to_try}")
    result1 = standardize_date(date1, formats_to_try)
    print(f"Standardized: {result1}\n")
    print(f"Input: {date2}, Formats: {formats_to_try}")
    result2 = standardize_date(date2, formats_to_try)
    print(f"Standardized: {result2}\n")
    print(f"Input: {date3}, Formats: {formats_to_try}")
    result3 = standardize_date(date3, formats_to_try)
    print(f"Standardized: {result3}\n")
    print(f"Input: {date4}, Formats: {formats_to_try}")
    result4 = standardize_date(date4, formats_to_try)
    print(f"Standardized: {result4}\n")
    print(f"Input: {invalid_date}, Formats: {formats_to_try}")
    result_invalid = standardize_date(invalid_date, formats_to_try)
    print(f"Standardized: {result_invalid}")