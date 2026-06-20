from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime(timestamp, "%B %d, %Y")
    days_until_monday = (target_date.weekday() - 0) % 7
    if days_until_monday == 0:
        return target_date.strftime("%B %d, %Y")
    else:
        return (target_date + timedelta(days=7 - days_until_monday)).strftime("%B %d, %Y")

if __name__ == '__main__':
    timestamp = "February 28, 2024"
    print(next_monday(timestamp))