import datetime

def get_current_day():
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days_of_week[today.weekday()]

if __name__ == '__main__':
    today = datetime.date.today()
    current_day = get_current_day()
    print(current_day)