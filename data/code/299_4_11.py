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
        '01/01/2024',
        '03/17/2024',
        '04/01/2024',
        '12/25/2023',
        '11/29/2023'
    ]
    for date in sample_dates:
        print(f"{date}: {is_weekend(date)}")