from datetime import datetime
def format_date_string(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%y').date()
        return date_object
    except ValueError:
        return None
if __name__ == '__main__':
    date_str_valid = "12/31/23"
    date_str_invalid = "32/01/23"
    date_str_wrong_format = "2023-12-31"
    result1 = format_date_string(date_str_valid)
    result2 = format_date_string(date_str_invalid)
    result3 = format_date_string(date_str_wrong_format)
    print(f"Input: {date_str_valid}, Result: {result1}")
    print(f"Input: {date_str_invalid}, Result: {result2}")
    print(f"Input: {date_str_wrong_format}, Result: {result3}")