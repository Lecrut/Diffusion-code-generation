from datetime import datetime

def convert_date_format(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%d.%m.%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    test_dates = ['12.05.2023', '01.01.2020', '31.12.2022']
    for date in test_dates:
        print(convert_date_format(date))