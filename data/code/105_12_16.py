from datetime import datetime, timedelta

def get_next_weekday(start_date_str, weekday):
    weekdays = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    target_weekday = weekdays[weekday]
    
    days_to_add = (target_weekday - start_date.weekday()) % 7
    
    next_date = start_date + timedelta(days=days_to_add)
    
    return next_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    start_date = "2023-10-01"
    weekday = "Friday"
    result = get_next_weekday(start_date, weekday)
    print(result)