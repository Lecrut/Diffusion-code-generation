import datetime
def calculate_time_remaining(current_date_str, target_month):
    current_date = datetime.datetime.strptime(current_date_str, "%Y-%m-%d").date()
    if target_month == 1:
        target_year = current_date.year
        target_month_num = 1
    else:
        target_year = current_date.year
        target_month_num = target_month
    if target_month_num < current_date.month:
        target_year -= 1
    target_date = datetime.date(target_year, target_month_num, 1)
    time_difference = target_date - current_date
    return time_difference.days
if __name__ == '__main__':
    current_date = "2023-10-15"
    target_month = 1
    time_left = calculate_time_remaining(current_date, target_month)
    print(time_left)