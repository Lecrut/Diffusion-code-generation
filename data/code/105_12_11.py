from datetime import datetime, timedelta

def is_valid_weekday(weekday):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday in weekdays

def get_next_weekday(start_date_str, target_weekday):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    target_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(target_weekday)
    
    while True:
        if is_valid_weekday(start_date.strftime("%A")) and start_date.weekday() == target_index:
            return start_date.strftime("%Y-%m-%d")
        start_date += timedelta(days=1)

if __name__ == '__main__':
    start_date = "2023-10-01"
    target_weekday = "Friday"
    result = get_next_weekday(start_date, target_weekday)
    print(result)