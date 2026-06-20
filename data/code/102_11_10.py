import datetime

def is_weekday(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-05'))
    print(is_weekday('2023-10-06'))