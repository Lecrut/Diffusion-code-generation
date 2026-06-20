from datetime import datetime

DATE_FORMAT_INPUT = '%Y-%m-%d'
DATE_FORMAT_OUTPUT = '%d/%m/%Y'

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, DATE_FORMAT_INPUT)
        return date_obj.strftime(DATE_FORMAT_OUTPUT)
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    sample_date = '2023-10-05'
    try:
        formatted_date = format_date(sample_date)
        print(formatted_date)
    except ValueError as e:
        print(e)