from datetime import datetime, timedelta

def days_remaining_in_month():
    today = datetime.now()
    _, num_days = monthrange(today.year, today.month)
    return num_days - today.day

if __name__ == '__main__':
    print(days_remaining_in_month())