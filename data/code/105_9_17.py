from datetime import datetime, timedelta

def next_monday(timestamp):
    target_date = datetime.strptime(timestamp, "%B %d, %Y")
    days_until_monday = (6 - target_date.weekday()) % 7 + 1
    return (target_date + timedelta(days=days_until_monday)).strftime("%B %d, %Y")

if __name__ == '__main__':
    sample_timestamp = "February 28, 2024"
    print(next_monday(sample_timestamp))