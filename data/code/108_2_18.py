import time

DAYS_IN_WEEK = 7
WEEKDAY_INDEX = 4
DAY_OF_MONTH_INDEX = 2

def extract_day_of_month():
    now = time.time()
    local_time = time.localtime(now)
    day = local_time[DAY_OF_MONTH_INDEX]
    return day

def format_day_output(day_value):
    formatted = f"Day of month: {day_value}"
    return formatted

if __name__ == '__main__':
    current_day = extract_day_of_month()
    output = format_day_output(current_day)
    print(output)