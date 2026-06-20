from datetime import datetime

def get_current_day_of_week():
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return week_days[datetime.now().weekday()]
if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_current_day_of_week(sample_date))