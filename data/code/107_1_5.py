from datetime import datetime

def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        return date_object.strftime('%d-%m-%Y')
    except ValueError:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    sample_dates = ['12/31/2023', '01/01/2024', '25/08/1999']
    for date_str in sample_dates:
        try:
            converted_date = convert_date_format(date_str)
            print(converted_date)
        except ValueError as e:
            print(e)