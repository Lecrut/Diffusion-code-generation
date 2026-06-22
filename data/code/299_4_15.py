import datetime

def is_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
        weekday = date_obj.weekday()
        if weekday >= 5:
            return True
        else:
            return False
    except ValueError:
        return None

if __name__ == '__main__':
    sample_dates = [
        '01/07/2024',
        '03/18/2024',
        '11/29/2023',
        '05/26/2024',
        '08/15/2024'
    ]
    for date in sample_dates:
        print(f"{date}: {is_weekend(date)}")