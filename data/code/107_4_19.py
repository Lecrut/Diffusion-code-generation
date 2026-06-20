from datetime import datetime

def reformat_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    test_dates = ['12.05.2023', '01.01.2020', '31.12.2022']
    for date in test_dates:
        print(reformat_date(date))