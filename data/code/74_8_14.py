import datetime

def get_current_day_of_week():
    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    today = datetime.date.today()
    return days_of_week[today.weekday()]

if __name__ == '__main__':
    print(get_current_day_of_week())