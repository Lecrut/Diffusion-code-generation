import datetime

def fetch_current_day():
    current_time = datetime.datetime.now()
    day_of_week = current_time.strftime("%A")
    return day_of_week

if __name__ == '__main__':
    sample_date = "2023-10-27"
    date_format = "%Y-%m-%d"
    
    try:
        date_object = datetime.datetime.strptime(sample_date, date_format)
        result = fetch_current_day()
        print(result)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")