import datetime

def get_current_day_of_week():
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    try:
        today = datetime.date.today()
        day_of_week = today.weekday()
        return days[day_of_week]
    except Exception as e:
        return f"Error determining the day of the week: {e}"

if __name__ == '__main__':
    day = get_current_day_of_week()
    print(day)