import datetime

def convert_date_format(date_string):
    DATE_INPUT_FORMAT = '%Y-%m-%d'
    DATE_OUTPUT_FORMAT = '%d/%m/%Y'
    
    try:
        date_obj = datetime.datetime.strptime(date_string, DATE_INPUT_FORMAT)
        return date_obj.strftime(DATE_OUTPUT_FORMAT)
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    sample_date = "2023-10-27"
    converted_date = convert_date_format(sample_date)
    print(converted_date)