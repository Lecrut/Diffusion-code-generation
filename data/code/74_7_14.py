import datetime

def get_current_day_of_week():
    try:
        current_date = datetime.datetime.now()
        return current_date.strftime("%A")
    except Exception as e:
        print(f"Error fetching day of week: {e}")
        return None

if __name__ == '__main__':
    print(get_current_day_of_week())