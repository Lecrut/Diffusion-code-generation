import datetime
import calendar

def get_day_of_week(year, month, day):
    try:
        calendar.timegm((year, month, day, 0, 0, 0))
    except (ValueError, OverflowError) as e:
        raise ValueError(f"Invalid date provided: {e}")
    
    date_instance = datetime.date(year, month, day)
    day_index = date_instance.weekday()
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[day_index]

if __name__ == '__main__':
    target_year = 1995
    target_month = 5
    target_day = 25
    weekday_result = get_day_of_week(target_year, target_month, target_day)
    print(weekday_result)