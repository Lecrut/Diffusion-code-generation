import datetime
def convert_date_format(date_str: str, from_format: str, to_format: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(date_str, from_format)
        return dt_object.strftime(to_format)
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}' with format '{from_format}': {e}")
if __name__ == '__main__':
    date1 = "2023/10/27"
    print(f"Original Date: {date1}")
    try:
        formatted_date = convert_date_format(date1, '%Y/%m/%d', '%m/%d/%Y')
        print(f"Converted to MM/DD/YYYY: {formatted_date}")
    except ValueError as e:
        print(f"Error: {e}")
    date2 = "12/31/2024"
    print(f"\nOriginal Date: {date2}")
    try:
        formatted_date = convert_date_format(date2, '%m/%d/%Y', '%Y/%m/%d')
        print(f"Converted to YYYY/MM/DD: {formatted_date}")
    except ValueError as e:
        print(f"Error: {e}")