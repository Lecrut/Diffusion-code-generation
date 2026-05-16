from datetime import datetime
def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%d-%m-%Y')
        iso_format = date_object.strftime('%Y-%m-%d')
        return iso_format
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    date_to_convert = '31-12-2023'
    iso_date = convert_date_format(date_to_convert)
    print(iso_date)