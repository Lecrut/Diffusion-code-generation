from datetime import datetime
def format_date_string(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%y').date()
        return date_object
    except ValueError:
        return None
if __name__ == '__main__':
    date_str_valid = "03/15/23"
    date_str_invalid = "2023-03-15"
    date_str_format_error = "15-03-2023"
    result_valid = format_date_string(date_str_valid)
    result_invalid = format_date_string(date_str_invalid)
    result_error = format_date_string(date_str_format_error)
    print(f"Input: {date_str_valid}, Result: {result_valid}")
    print(f"Input: {date_str_invalid}, Result: {result_invalid}")
    print(f"Input: {date_str_format_error}, Result: {result_error}")