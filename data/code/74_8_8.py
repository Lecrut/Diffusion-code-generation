import datetime

def get_current_day_of_week():
    try:
        now = datetime.datetime.now()
        day_of_week = now.strftime("%A")
        return day_of_week
    except Exception as e:
        raise ValueError("Failed to determine the current day of the week") from e

if __name__ == '__main__':
    print(get_current_day_of_week())