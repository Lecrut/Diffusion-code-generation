from datetime import datetime, timedelta

def next_day_of_week(target_date, day_name):
    target = datetime.strptime(target_date, "%B %d, %Y")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    target_day_index = days.index(day_name)
    current_day_index = target.weekday()
    
    if current_day_index >= target_day_index:
        days_until_next = (target_day_index + 7 - current_day_index) % 7
    else:
        days_until_next = target_day_index - current_day_index
    
    next_date = target + timedelta(days=days_until_next)
    return next_date.strftime("%B %d, %Y")

if __name__ == '__main__':
    print(next_day_of_week("September 15, 2023", "Thursday"))