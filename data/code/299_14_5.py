import datetime

def check_weekday_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        day_of_week = date_obj.weekday()
        return "weekend" if day_of_week >= 5 else "weekday"
    except ValueError:
        return None

if __name__ == '__main__':
    sample_dates = {
        "2023-10-27": "Saturday",
        "2023-10-28": "Sunday",
        "2024-01-01": "Friday",
        "2024-01-07": "Thursday"
    }

    for date_str, expected in sample_dates.items():
        result = check_weekday_weekend(date_str)
        print(f"The date {date_str} is a {result}. Expected: {expected}")