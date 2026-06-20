import datetime

def get_current_day_of_week():
    try:
        now = datetime.datetime.now()
        return now.strftime("%A")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    day_of_week = get_current_day_of_week()
    if day_of_week is not None:
        print(day_of_week)