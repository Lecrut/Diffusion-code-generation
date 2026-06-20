import datetime

def get_current_day():
    return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][datetime.date.today().weekday()]

if __name__ == '__main__':
    day = get_current_day()
    print(day)