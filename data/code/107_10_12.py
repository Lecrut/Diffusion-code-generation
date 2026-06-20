from datetime import datetime
INPUT_DATE_FORMAT = '%Y-%m-%d'
OUTPUT_DATE_FORMAT = '%d/%m/%Y'

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, INPUT_DATE_FORMAT)
        return date_obj.strftime(OUTPUT_DATE_FORMAT)
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
if __name__ == '__main__':
    sample_date = '2023-10-05'
    try:
        formatted_date = format_date(sample_date)
        print(formatted_date)
    except ValueError as e:
        print(e)