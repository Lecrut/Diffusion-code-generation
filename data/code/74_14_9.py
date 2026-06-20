import datetime

def get_current_day_of_week():
    current_date = datetime.datetime.now()
    day_of_week = current_date.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    sample_date = "2023-11-05"
    date_object = datetime.datetime.strptime(sample_date, "%Y-%m-%d")
    day_of_week_str = get_current_day_of_week()
    print(day_of_week_str)