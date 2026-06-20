from datetime import datetime

def get_current_day_of_week():
    try:
        current_date = datetime.now()
        day_of_week = current_date.strftime('%A')
        return day_of_week
    except Exception as e:
        raise ValueError("Failed to determine current day of the week") from e

if __name__ == '__main__':
    print(get_current_day_of_week())