from datetime import datetime

def get_current_day():
    current_date = datetime.now()
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days_of_week[current_date.weekday()]

if __name__ == '__main__':
    print(get_current_day())