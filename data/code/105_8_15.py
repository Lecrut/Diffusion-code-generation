from datetime import datetime, timedelta

def next_day_of_week(target_date, target_day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    target_index = days.index(target_day)
    current_index = target_date.weekday()
    delta = (target_index - current_index) % 7
    if delta == 0:
        delta = 7
    return target_date + timedelta(days=delta)

if __name__ == '__main__':
    sample_date = datetime(2023, 9, 15)
    target_day = "Thursday"
    next_thursday = next_day_of_week(sample_date, target_day)
    print(next_thursday.strftime("%Y-%m-%d"))