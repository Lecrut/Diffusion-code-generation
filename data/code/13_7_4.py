import datetime
def calculate_duration(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d")
    duration = date2 - date1
    return duration.days
if __name__ == '__main__':
    start_date = "2020-03-01"
    end_date = "2024-03-01"
    duration = calculate_duration(start_date, end_date)
    print(duration)