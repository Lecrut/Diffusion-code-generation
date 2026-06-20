from datetime import datetime

def get_current_day_of_week():
    day_index = datetime.now().weekday()
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    return days[day_index]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    day_of_week = get_current_day_of_week()
    print(f"The current day of the week is: {day_of_week}")