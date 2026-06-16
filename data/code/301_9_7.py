import datetime
def convert_date_format(date_str: str, from_format: str, to_format: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(date_str, from_format)
        return dt_object.strftime(to_format)
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}' with format '{from_format}': {e}")
if __name__ == '__main__':
    date1 = "2023/10/27"
    date2 = "10/27/2023"
    print(f"Original Date 1 (YYYY/MM/DD): {date1}")
    converted_to_mdy1 = convert_date_format(date1, '%Y/%m/%d', '%m/%d/%Y')
    print(f"Converted to MM/DD/YYYY: {converted_to_mdy1}\n")
    print(f"Original Date 2 (MM/DD/YYYY): {date2}")
    converted_to_ymd2 = convert_date_format(date2, '%m/%d/%Y', '%Y/%m/%d')
    print(f"Converted to YYYY/MM/DD: {converted_to_ymd2}\n")
    try:
        convert_date_format("2023-10-27", '%Y/%m/%d', '%m/%d/%Y')
    except ValueError as e:
        print(f"Error caught successfully: {e}")