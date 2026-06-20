from datetime import datetime

def convert_date_format(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%d.%m.%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    test_dates = ['15.08.2023', '25.12.2021', '07.04.2020']
    for date in test_dates:
        result = convert_date_format(date)
        print(result)