import datetime
def convert_date_format(date_str: str, from_format: str, to_format: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(date_str, from_format)
        return dt_object.strftime(to_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format or value provided: {e}")
if __name__ == '__main__':
    date1 = "2023/10/27"
    print(f"Original Date: {date1}")
    try:
        converted_to_mdy = convert_date_format(date1, "%Y/%m/%d", "%m/%d/%Y")
        print(f"Converted to MM/DD/YYYY: {converted_to_mdy}")
    except ValueError as e:
        print(f"Error processing date1: {e}")
    date2 = "11/05/2024"
    print(f"\nOriginal Date: {date2}")
    try:
        converted_to_ymd = convert_date_format(date2, "%m/%d/%Y", "%Y/%m/%d")
        print(f"Converted to YYYY/MM/DD: {converted_to_ymd}")
    except ValueError as e:
        print(f"Error processing date2: {e}")
    date3 = "2025/01/01"
    print(f"\nOriginal Date: {date3}")
    try:
        converted_to_mdy_again = convert_date_format(date3, "%Y/%m/%d", "%m/%d/%Y")
        print(f"Converted to MM/DD/YYYY: {converted_to_mdy_again}")
    except ValueError as e:
        print(f"Error processing date3: {e}")