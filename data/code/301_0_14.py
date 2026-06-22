from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_date = '2024-01-01'
    converted_date = convert_date_format(sample_date)
    print(converted_date)