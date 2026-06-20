import datetime

def find_next_day_of_week(start_date, target_day):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_index = days.index(start_date.strftime("%A"))
    target_index = days.index(target_day)
    days_difference = (target_index - start_index) % 7
    next_date = start_date + datetime.timedelta(days=days_difference)
    return next_date

if __name__ == '__main__':
    sample_start_date = datetime.datetime(2023, 9, 15)
    target_day = "Thursday"
    result_date = find_next_day_of_week(sample_start_date, target_day)
    print(result_date.strftime("%Y-%m-%d"))