from datetime import datetime

def get_day_of_month(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.day

if __name__ == '__main__':
    dates = ['2023-10-05', '2023-11-15', '2023-12-25']
    for date in dates:
        print(get_day_of_month(date))