from datetime import datetime

def transform_date(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%d.%m.%Y')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date = '25.12.2023'
    result = transform_date(sample_date)
    print(result)