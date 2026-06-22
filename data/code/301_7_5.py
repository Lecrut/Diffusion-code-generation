from datetime import datetime

def get_day_of_week(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%A')

if __name__ == '__main__':
    print(get_day_of_week('2023-10-05'))