from datetime import datetime, timedelta

def next_monday(timestamp):
    date = datetime.strptime(timestamp, "%B %d, %Y")
    days_until_monday = (date.weekday() - 0) % 7
    return (date + timedelta(days=days_until_monday)).strftime("%B %d, %Y")

if __name__ == '__main__':
    sample_timestamp = "February 28, 2024"
    print(next_monday(sample_timestamp))