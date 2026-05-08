import datetime
def get_day_of_month(date_string):
    formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d",
        "%m-%d-%Y",
        "%d/%m/%Y",
        "%Y%m%d"
    ]
    for fmt in formats:
        try:
            date_obj = datetime.datetime.strptime(date_string, fmt)
            return date_obj.day
        except ValueError:
            continue
    raise ValueError(f"Date format not recognized for input: {date_string}")
if __name__ == '__main__':
    test_dates = [
        "2023-10-27",
        "10/27/2023",
        "27-10-2023",
        "2023/10/27",
        "10-27-2023",
        "27/10/2023",
        "20231027",
        "2023-12-31"
    ]
    for date_str in test_dates:
        try:
            day = get_day_of_month(date_str)
            print(f"Input: {date_str}, Day of Month: {day}")
        except ValueError as e:
            print(f"Error processing {date_str}: {e}")