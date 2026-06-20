from datetime import datetime

def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_name = date_obj.strftime('%A').upper()
    return day_name

if __name__ == '__main__':
    sample_date = '2023-11-11'
    print(get_day_of_week(sample_date))