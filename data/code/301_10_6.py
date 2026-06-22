import datetime

def convert_date_format(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    sample_date = "2023-10-27"
    converted_date = convert_date_format(sample_date)
    print(converted_date)