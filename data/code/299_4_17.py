import datetime

def check_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        day_of_week = date_obj.weekday()
        return day_of_week >= 5
    except ValueError:
        return False

if __name__ == '__main__':
    dates_to_check = [
        '01/01/2024',
        '01/06/2024',
        '03/15/2024',
        '12/25/2023',
        '02/17/2024'
    ]
    
    for date in dates_to_check:
        print(f"{date}: {check_weekend(date)}")