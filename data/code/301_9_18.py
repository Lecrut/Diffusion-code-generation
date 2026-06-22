import datetime

class DateFormatter:
    INPUT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"
    OUTPUT_FORMAT = "%d-%b-%Y %I:%M %p"

    @staticmethod
    def convert(date_str: str) -> str:
        try:
            dt_object = datetime.datetime.strptime(date_str, DateFormatter.INPUT_FORMAT)
            return dt_object.strftime(DateFormatter.OUTPUT_FORMAT)
        except ValueError as e:
            raise ValueError(f"Error parsing date '{date_str}' with format '{DateFormatter.INPUT_FORMAT}': {e}")

if __name__ == '__main__':
    date1 = "2023-10-27T15:30:45.678901+02:00"
    print(f"Original Date: {date1}")
    try:
        formatted_date_1 = DateFormatter.convert(date1)
        print(f"Converted to DD-Mon-YYYY HH:MM AM/PM: {formatted_date_1}")
    except ValueError as e:
        print(f"Error processing date 1: {e}")

    date2 = "2024-11-05T09:15:30.123456+03:00"
    print(f"\nOriginal Date: {date2}")
    try:
        formatted_date_2 = DateFormatter.convert(date2)
        print(f"Converted to DD-Mon-YYYY HH:MM AM/PM: {formatted_date_2}")
    except ValueError as e:
        print(f"Error processing date 2: {e}")