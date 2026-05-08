from datetime import datetime
def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%d-%m-%Y')
        iso_format = date_object.strftime('%Y-%m-%d')
        return iso_format
    except ValueError:
        return "Invalid date format"
if __name__ == '__main__':
    date_str1 = "31-12-2023"
    date_str2 = "01-01-2024"
    date_str3 = "25-08-1999"
    print(convert_date_format(date_str1))
    print(convert_date_format(date_str2))
    print(convert_date_format(date_str3))