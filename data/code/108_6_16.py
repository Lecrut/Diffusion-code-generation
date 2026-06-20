from datetime import datetime

def get_day_of_month(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').day

if __name__ == '__main__':
    dates = ['2023-10-05', '2023-11-15', '2023-12-25']
    for date in dates:
        print(get_day_of_month(date))