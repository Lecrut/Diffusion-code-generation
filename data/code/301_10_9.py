import datetime

def convert_date_format(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    sample_date = "1999-04-30"
    converted_date = convert_date_format(sample_date)
    print(converted_date)