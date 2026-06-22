from datetime import datetime

def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converted_date = convert_date_format(sample_date)
    print(converted_date)