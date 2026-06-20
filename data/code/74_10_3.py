from datetime import datetime

def get_current_day():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[datetime.now().weekday()]

if __name__ == '__main__':
    print(get_current_day())