from datetime import datetime

def get_full_day_name(date_obj):
    day_names = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    return day_names[date_obj.weekday()]

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(get_full_day_name(sample_date))