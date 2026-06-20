from datetime import datetime

def reformat_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_dates = ['25.12.2023', '01.01.2022', '31.07.2021']
    for date in sample_dates:
        result = reformat_date(date)
        print(result)