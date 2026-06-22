from datetime import datetime

def check_for_weekdays(date_strings):
    weekday_dates = []
    for date_str in date_strings:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
        if parsed_date.weekday() < 5:
            weekday_dates.append(date_str)
    return weekday_dates

if __name__ == '__main__':
    input_dates = ["2024-01-15", "2024-01-20", "2024-01-21", "2024-01-27"]
    found_weekdays = check_for_weekdays(input_dates)
    print(found_weekdays)