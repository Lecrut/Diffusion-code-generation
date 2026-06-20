from datetime import datetime, timedelta

def next_occurrence(day_of_week, start_date):
    target_day = datetime.strptime(start_date, "%B %d, %Y").weekday()
    days_until_target = (target_day - datetime.strptime(start_date, "%B %d, %Y").weekday() + 7) % 7
    if days_until_target == 0:
        days_until_target = 7
    next_date = datetime.strptime(start_date, "%B %d, %Y") + timedelta(days=days_until_target)
    return next_date.strftime("%B %d, %Y")

if __name__ == '__main__':
    print(next_occurrence("Thursday", "September 15, 2023"))