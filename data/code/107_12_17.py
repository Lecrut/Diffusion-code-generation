from datetime import datetime

def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%b-%Y')
        return date_obj.strftime('%Y%m%d')
    except ValueError:
        return None

if __name__ == '__main__':
    sample_date = '10-Mar-2023'
    result = convert_date_format(sample_date)
    print(f"'{sample_date}' converted: {result}")