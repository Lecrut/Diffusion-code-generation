from datetime import datetime

def get_current_day():
    days_of_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    current_day_index = datetime.now().weekday()
    return days_of_week[current_day_index]
if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_current_day())