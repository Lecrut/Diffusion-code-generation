import datetime

DAY_NAMES = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def get_date_info(year, month, day):
    target_date = datetime.date(year, month, day)
    day_of_week_index = target_date.weekday()
    return target_date.strftime("%B %d, %Y"), DAY_NAMES[day_of_week_index]

if __name__ == '__main__':
    year_val = 2024
    month_val = 1
    day_val = 1
    full_date_str, day_str = get_date_info(year_val, month_val, day_val)
    print(day_str)