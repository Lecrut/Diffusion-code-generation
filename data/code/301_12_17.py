from datetime import datetime

DATE_FORMAT_INPUT = "%Y-%m-%d"
DATE_FORMAT_OUTPUT = "%A, %B %d, %Y"

def convert_date(date_string):
    try:
        date_object = datetime.strptime(date_string, DATE_FORMAT_INPUT)
        converted_date = date_object.strftime(DATE_FORMAT_OUTPUT)
        return converted_date
    except ValueError as e:
        return f"Error: Invalid date format or string provided. Details: {e}"

if __name__ == '__main__':
    date_str_1 = "2023-12-31"
    result_1 = convert_date(date_str_1)
    print(f"Input: {date_str_1} ({DATE_FORMAT_INPUT}) -> Output: {result_1}")