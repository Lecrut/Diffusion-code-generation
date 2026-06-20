from datetime import datetime

def get_current_day_of_week():
    return datetime.now().strftime('%A')
if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print('Current day of the week:', get_current_day_of_week())