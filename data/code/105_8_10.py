from datetime import datetime, timedelta

def next_day_of_week(start_date, target_day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_index = days.index(start_date.strftime("%A"))
    target_index = days.index(target_day)
    days_difference = (target_index - start_index) % 7
    return start_date + timedelta(days=days_difference)

if __name__ == '__main__':
    start_date = datetime(2023, 9, 15)
    target_day = "Thursday"
    result = next_day_of_week(start_date, target_day)
    print(result.strftime("%Y-%m-%d"))