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
    date1 = '12/31/2023'
    date2 = '2024-01-15'
    date3 = '05/20/2022'
    date4 = '2023/10/01'
    invalid_date = '2023-13-01'
    formats_to_try = ['%m/%d/%Y', '%Y-%m-%d', '%d/%m/%Y', '%Y/%m/%d']
    print(f"Input: {date1}, Standardized: {standardize_date_format(date1, formats_to_try)}")
    print(f"Input: {date2}, Standardized: {standardize_date_format(date2, formats_to_try)}")
    print(f"Input: {date3}, Standardized: {standardize_date_format(date3, formats_to_try)}")
    print(f"Input: {date4}, Standardized: {standardize_date_format(date4, formats_to_try)}")
    print(f"Input: {invalid_date}, Standardized: {standardize_date_format(invalid_date, formats_to_try)}")