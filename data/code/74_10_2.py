from datetime import datetime

days_of_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_current_day():
    current_day_index = datetime.now().weekday()
    return days_of_week[current_day_index]

if __name__ == '__main__':
    print(get_current_day())