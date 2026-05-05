import datetime
def get_current_day_of_week():
    try:
        today = datetime.date.today()
        day_of_week = today.weekday()
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return days[day_of_week]
    except Exception as e:
        return f"An error occurred: {e}"
if __name__ == '__main__':
    result = get_current_day_of_week()
    print(result)