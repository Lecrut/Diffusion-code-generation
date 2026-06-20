import datetime

def get_current_day_of_week():
    try:
        today = datetime.date.today()
        day_name = today.strftime("%A")
        return day_name
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    print(get_current_day_of_week())