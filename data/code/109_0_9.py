from datetime import datetime

def days_remaining_in_month():
    today = datetime.now()
    _, last_day = calendar.monthrange(today.year, today.month)
    return last_day - today.day

if __name__ == '__main__':
    print(days_remaining_in_month())