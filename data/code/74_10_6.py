from datetime import datetime

def get_current_day():
    week_map = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return week_map[datetime.now().weekday()]

if __name__ == '__main__':
    print(get_current_day())