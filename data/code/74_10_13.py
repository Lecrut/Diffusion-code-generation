from datetime import datetime

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_current_day():
    current_weekday_index = datetime.now().weekday()
    return DAYS_OF_WEEK[current_weekday_index]

if __name__ == '__main__':
    print(get_current_day())