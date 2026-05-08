from datetime import datetime
def format_date_string(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%y').date()
        return date_object
    except ValueError:
        return None
if __name__ == '__main__':
    date_str_valid = "12/31/23"
    date_str_invalid = "2023-12-31"
    date_str_format_error = "31/12/23"
    result_valid = format_date_string(date_str_valid)
    result_invalid = format_date_string(date_str_invalid)
    result_format_error = format_date_string(date_str_format_error)
    print(f"Input: {date_str_valid}, Result: {result_valid}")
    print(f"Input: {date_str_invalid}, Result: {result_invalid}")
    print(f"Input: {date_str_format_error}, Result: {result_format_error}")