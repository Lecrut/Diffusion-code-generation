import datetime

def fetch_current_day_of_week():
    current_time = datetime.datetime.now()
    day_of_week = current_time.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    sample_date = "2023-11-05"
    date_object = datetime.datetime.strptime(sample_date, "%Y-%m-%d")
    result = fetch_current_day_of_week()
    print(result)