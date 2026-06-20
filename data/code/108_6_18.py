import datetime

def get_day_of_month(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.day
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    dates = ["2023-10-05", "2023-02-29", "2023-11-30"]
    for date in dates:
        print(f"{date} is day {get_day_of_month(date)} of the month.")