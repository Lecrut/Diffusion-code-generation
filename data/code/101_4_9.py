from datetime import datetime

def day_of_week(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').weekday()
if __name__ == '__main__':
    print(day_of_week('2023-10-05'))