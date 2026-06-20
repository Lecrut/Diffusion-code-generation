import datetime

def get_day_of_month(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.day

if __name__ == '__main__':
    dates = ['2023-10-05', '2023-11-15', '2023-12-25']
    results = [get_day_of_month(date) for date in dates]
    print(results)