import datetime

def find_first_weekday(date_strings):
    for date_str in date_strings:
        parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        if parsed_date.weekday() < 5:
            return date_str
    return None

if __name__ == '__main__':
    dates = ["2023-10-07", "2023-10-08", "2023-10-09"]
    result = find_first_weekday(dates)
    print(result)