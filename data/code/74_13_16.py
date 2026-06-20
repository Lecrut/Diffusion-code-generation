from datetime import datetime

def get_current_day_of_week():
    try:
        now = datetime.now()
        day_of_week_number = now.weekday()
        days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return days[day_of_week_number]
    except Exception as e:
        raise ValueError("Failed to determine current day of the week") from e

if __name__ == '__main__':
    print(get_current_day_of_week())