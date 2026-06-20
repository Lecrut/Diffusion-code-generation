from datetime import datetime

DAYS_OF_WEEK = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def get_current_day():
    return DAYS_OF_WEEK[datetime.now().weekday()]

if __name__ == '__main__':
    print(get_current_day())