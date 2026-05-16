import datetime
def get_current_day_of_week():
    try:
        today = datetime.date.today()
        day_name = today.strftime("%A")
        return day_name
    except Exception:
        return "Error determining the day of the week"
if __name__ == '__main__':
    day = get_current_day_of_week()
    print(day)