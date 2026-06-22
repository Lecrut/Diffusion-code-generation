import time

def get_weekday_for_date(date_str):
    struct_time = time.strptime(date_str, "%Y-%m-%d")
    epoch_seconds = time.mktime(struct_time)
    time_info = time.localtime(epoch_seconds)
    day_of_week_code = time_info.tm_wday
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return day_names[day_of_week_code]

if __name__ == '__main__':
    query_date = '2023-01-01'
    computed_day = get_weekday_for_date(query_date)
    print(computed_day)