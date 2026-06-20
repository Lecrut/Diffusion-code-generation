from datetime import datetime

def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        iso_format = date_object.strftime('%d-%m-%Y')
        return iso_format
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_dates = ['12/31/2023', '01/01/2024', '25/08/1999']
    for date in sample_dates:
        print(convert_date_format(date))