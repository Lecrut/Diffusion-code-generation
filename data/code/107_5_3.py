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
    date_str_format_error = "15/03/23"
    result1 = format_date_string(date_str_valid)
    result2 = format_date_string(date_str_invalid)
    result3 = format_date_string(date_str_format_error)
    print(f"Input: {date_str_valid}, Result: {result1}, Type: {type(result1)}")
    print(f"Input: {date_str_invalid}, Result: {result2}, Type: {type(result2)}")
    print(f"Input: {date_str_format_error}, Result: {result3}, Type: {type(result3)}")