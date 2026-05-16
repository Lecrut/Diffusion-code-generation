import datetime
def get_day_of_month(date_string):
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%m-%d-%Y"
    ]
    for fmt in formats:
        try:
            dt_object = datetime.datetime.strptime(date_string, fmt)
            return dt_object.day
        except ValueError:
            continue
    raise ValueError(f"Could not parse date string: {date_string}")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "10/27/2023",
        "27-10-2023",
        "2023/10/27",
        "11-05-2024",
        "invalid-date"
    ]
    for date_str in sample_dates:
        try:
            day = get_day_of_month(date_str)
            print(f"Input: {date_str}, Day of Month: {day}")
        except ValueError as e:
            print(f"Input: {date_str}, Error: {e}")
        except Exception as e:
            print(f"Input: {date_str}, Unexpected Error: {e}")