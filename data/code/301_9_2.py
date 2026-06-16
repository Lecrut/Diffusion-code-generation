import datetime
def convert_date_format(date_str: str, from_format: str, to_format: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(date_str, from_format)
        new_date_str = dt_object.strftime(to_format)
        return new_date_str
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}' with format '{from_format}': {e}")
if __name__ == '__main__':
    date1 = "2023/10/27"
    print(f"Original Date (YYYY/MM/DD): {date1}")
    try:
        formatted_date2 = convert_date_format(date1, '%Y/%m/%d', '%m/%d/%Y')
        print(f"Converted Date (MM/DD/YYYY): {formatted_date2}")
    except ValueError as e:
        print(f"Conversion Error: {e}")
    date3 = "11/15/2024"
    print(f"\nOriginal Date (MM/DD/YYYY): {date3}")
    try:
        formatted_date1 = convert_date_format(date3, '%m/%d/%Y', '%Y/%m/%d')
        print(f"Converted Date (YYYY/MM/DD): {formatted_date1}")
    except ValueError as e:
        print(f"Conversion Error: {e}")